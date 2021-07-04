#executar na mesma pasta que o video e com OpenCV instalado!!!
#nome: Eduardo Bruno Martins Esperança
#data: 3/07/2021
#programa de filtragem de ruido e conversor para grayscale
 
import cv2
import numpy as np
import os
 
 
 
def conversor(fps, currentFrame):
    
    #criamos um array para guardar as imagens
    img_array = []
 
    #pelo for vamos pegar seus respectivos numeros e armazenalas em ordem cronologica
    for filename in range(0,currentFrame,1):
        frame = cv2.imread('./data/' + str(filename)+ '.jpg')
        altura, largura, layers = frame.shape
        tamanho = (largura,altura)
        img_array.append(frame)
 
    #juntando todo o array e formando um video, com o numero de frames do video original e proporções do original
    video = cv2.VideoWriter('VIDEO_2021_FILTRADO.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, tamanho)
 
    for imagem in range(len(img_array)):
        video.write(img_array[imagem])
 
    #finalizando os processos
    video.release()
 
    return
 
# iniciado o video do arquivo
vid = cv2.VideoCapture('VIDEO_2021.mp4')
 
#verifica se existe diretorio para os frames
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Erro: video nao encontrado')
 
fps= vid.get(cv2.CAP_PROP_FPS)
 
currentFrame = 0
 
 
while (True):
    # pegando frame a frame
    ret, frame = vid.read()
 
    if frame is None:
        print ('fim do processamento')
        break
    
    ##pegamos o frame e passamos pelo filtro median para tirar o ruido, usando uma proporcao de cálculo de mediana em matrizes 7x7
 
    median = cv2.medianBlur(frame,3)
    
    #salva o frames em jpg
 
    name = './data/' + str(currentFrame) + 'N' + '.jpg'
    
    cv2.imwrite(name, median)
 
    #convertendo para gray scale
    gray = cv2.imread( name, 0)
 
    #salva a do tipo gray scale
 
    saved = './data/' + str(currentFrame) + '.jpg'
 
    cv2.imwrite(saved, gray)
 
    #deletando as do tipo normal
    try: 
       os.remove(name)
    except: 
       pass
    
    #contador  indo pro proximo frame
    currentFrame +=1
 
 
 
print ('Numero de Quadros = ', currentFrame ,'// Frames por segundo=',fps)
 
#fechando os processos 
vid.release()
 
#chamando funcao auxiliar que forma o video em tipo .avi
conversor(fps, currentFrame)
 
#fim do programa
 
 
 
 
