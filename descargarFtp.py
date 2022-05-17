import time
import threading
import ftplib
import os

#Variables
log=time.strftime("%H%M-%Y-%m-%d")
path_server_remoto="ftp.dominio_url'
ruta_carpeta_servidor='/public_html/tribunalelectoralchiapas.gob.mx'
path_server_local='//192.168.1.16//informatica//respaldo_pagina'
usuario_ftp='Escribe usuario del ftp'
pass_ftp='Escribe la contraseña ftp'
#Creamos una lista con los nombres de archivo
archivos=['Agrega Nombres Archivo','index.php','estradosElectronicos.php','sentencias.php','listado_acuerdos.php'];
#conexión al servidor
ftp = ftplib.FTP(path_server_remoto,usuario_ftp, pass_ftp)
ftp.enconding="utf-8"
ftp.cwd(ruta_carpeta_servidor)
#creamos la carpeta del backup
os.mkdir(log)
os.chdir(log)
#Iterar en los nombres de la lista
for archivo in archivos:
  print(archivo)
  log_archivo=log+'-'+archivo
  ftp.retrbinary("RETR " +archivo, open(log_archivo,'wb').write)
ftp.quit()
#ftp.retrlines("LIST")



    
    
