#!/usr/bin/python
import os
dir_list = ['2017','2018','2019']
active_dir = os.getcwd()

def listarDiretorios(ls, tabcount):
  if ls:
    for arquivo in ls:
      if os.path.isdir(arquivo):
        print('%s%s - Diretorio' %(('\t' * tabcount),arquivo))
        os.chdir(arquivo)
        listarDiretorios(os.listdir(), (tabcount+1))
      else:
        print('%s%s' %('\t' * tabcount,arquivo))
    os.chdir('..')
  else:
    os.chdir('..')

listarDiretorios(os.listdir(),1)

def criarSubPastas(pastas):
  your_dir = os.getcwd()
  for mes in pastas:  # Aqui eu estou criando as pastas ditas pelo usuario
    next_path = nextDir(mes)
    os.makedirs(next_path)
    os.chdir(next_path)
    for num_mes in range(1,13):   # Aqui eu começo a criar pastas do 1 ao 12
      next_path = nextDir(num_mes)
      os.makedirs(next_path)
      os.chdir(next_path)
      for num_dias in range(1,32):  # Agora, percorro a quantidade de dias no mes
        if num_mes == 2 & num_dias > 28:
          break
        
        if num_dias == 31:
          if ((num_mes % 2) == 0 & num_mes < 8) | ((num_mes%2) == 1 & num_mes >= 8):
            break

        os.makedirs(str(num_dias)) # E, finalmente, crio a pasta final
      
      os.chdir('..')
    os.chdir('..') 
  
def nextDir(dir_name):
  return os.path.join(os.getcwd(),str(dir_name))

