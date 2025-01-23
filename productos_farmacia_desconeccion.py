# -*- coding: utf-8 -*-
"""Productos_farmacia_desconeccion

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11kqZMpJ0iVNeokvVWkaJkwipaEbaZSSz

PRODUCTOS DE FARMACIA PARA WEB SCRAPING


Librerias
"""
import subprocess

# Ejecutar un comando de shell
def run_shell_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error ejecutando el comando: {stderr.decode('utf-8')}")
    else:
        print(stdout.decode('utf-8'))

# Ejemplo de uso:
run_shell_command('apt-get install git')

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time
import random
import os

# Lista de URLs
urls = ['https://www.alfabeta.net/precio/lisaler.html',
'https://www.alfabeta.net/precio/losacor.html',
'https://www.alfabeta.net/precio/lotrial.html',
'https://www.alfabeta.net/precio/macril.html',
'https://www.alfabeta.net/precio/manzan.html',
'https://www.alfabeta.net/precio/marathon.html',
'https://www.alfabeta.net/precio/megalex.html',
'https://www.alfabeta.net/precio/meridian.html',
'https://www.alfabeta.net/precio/meropenem-fabra.html',
'https://www.alfabeta.net/precio/metaflex-50.html',
'https://www.alfabeta.net/precio/metral.html',
'https://www.alfabeta.net/precio/micardis.html',
'https://www.alfabeta.net/precio/micolis.html',
'https://www.alfabeta.net/precio/midax.html',
'https://www.alfabeta.net/precio/miolox.html',
'https://www.alfabeta.net/precio/mylanta.html',
'https://www.alfabeta.net/precio/naprux.html',
'https://www.alfabeta.net/precio/neumoterol-200.html',
'https://www.alfabeta.net/precio/norfloxacina-richet.html',
'https://www.alfabeta.net/precio/novalgina.html',
'https://www.alfabeta.net/precio/novasone.html',
'https://www.alfabeta.net/precio/novo-alerpriv.html',
'https://www.alfabeta.net/precio/omega-3-duo-vitamin-way.html',
'https://www.alfabeta.net/precio/otosporin-dexa.html',
'https://www.alfabeta.net/precio/oxa-gel.html',
'https://www.alfabeta.net/precio/palatrobil.html',
'https://www.alfabeta.net/precio/paracetamol-raffo-500.html',
'https://www.alfabeta.net/precio/penicilina-g-benzatinica.html',
'https://www.alfabeta.net/precio/pharmaton-50--omega-3.html',
'https://www.alfabeta.net/precio/pharmaton-nf.html',
'https://www.alfabeta.net/precio/piroxicam-relax.html',
'https://www.alfabeta.net/precio/platsula.html',
'https://www.alfabeta.net/precio/plenacor.html',
'https://www.alfabeta.net/precio/pradaxa.html',
'https://www.alfabeta.net/precio/prurisedan.html',
'https://www.alfabeta.net/precio/quelat-complex.html',
'https://www.alfabeta.net/precio/qura-plus.html',
'https://www.alfabeta.net/precio/raquiferol-d3.html',
'https://www.alfabeta.net/precio/redoxitos-naranja-masticables.html',
'https://www.alfabeta.net/precio/redoxon.html',
'https://www.alfabeta.net/precio/reliveran.html',
'https://www.alfabeta.net/precio/risperdal.html',
'https://www.alfabeta.net/precio/rovartal.html',
'https://www.alfabeta.net/precio/salicrem-arnica-y-andiroba.html',
'https://www.alfabeta.net/precio/salofalk.html',
'https://www.alfabeta.net/precio/salvalerg.html',
'https://www.alfabeta.net/precio/seretide-aerosol-hfa.html',
'https://www.alfabeta.net/precio/sertal-compuesto.html',
'https://www.alfabeta.net/precio/siblix.html',
'https://www.alfabeta.net/precio/sinac-pb.html',
'https://www.alfabeta.net/precio/solocalm.html',
'https://www.alfabeta.net/precio/sultamicilina-richet.html',
'https://www.alfabeta.net/precio/supradyn-efervescente.html',
'https://www.alfabeta.net/precio/supragesic-t-nf.html',
'https://www.alfabeta.net/precio/symbicort-turbuhaler.html',
'https://www.alfabeta.net/precio/tafirol-forte.html',
'https://www.alfabeta.net/precio/taural-f-20.html',
'https://www.alfabeta.net/precio/tensimed.html',
'https://www.alfabeta.net/precio/total-magnesiano-energizante.html',
'https://www.alfabeta.net/precio/trapax.html',
'https://www.alfabeta.net/precio/unesia.html',
'https://www.alfabeta.net/precio/unicalm.html',
'https://www.alfabeta.net/precio/uvasal.html',
'https://www.alfabeta.net/precio/valcote.html',
'https://www.alfabeta.net/precio/vasotenal.html',
'https://www.alfabeta.net/precio/verboril.html',
'https://www.alfabeta.net/precio/zitromax.html',
'https://www.alfabeta.net/precio/zyrtec.html',
]

# Inicialización de variables globales
archivo_csv = "productos_scrapeados.csv"
contador = 0

# Función para guardar datos en un archivo CSV
def guardar_datos_csv(df, archivo):
    if not os.path.exists(archivo):
        df.to_csv(archivo, index=False)
    else:
        df.to_csv(archivo, mode='a', index=False, header=False)

# Función de scraping
def scrap(url):
    global contador

    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    datos = {
        'producto': [item.get_text(strip=True) for item in soup.find_all("span", class_="tproducto")],
        'presentacion': [item.get_text(strip=True) for item in soup.find_all("td", class_="tddesc")],
        'laboratorio': [item.get_text(strip=True) for item in soup.find_all("span", class_="defecto")],
        'precio': [item.get_text(strip=True) for item in soup.find_all("td", class_="tdprecio")],
        'fecha': [item.get_text(strip=True) for item in soup.find_all("td", class_="tdfecha")]
    }

    producto_info = {
        "presentacion": datos["presentacion"],
        "precios": datos["precio"],
        "fecha_ultimo_precio": datos["fecha"]
    }

    pd_datos_extraidos = pd.DataFrame(producto_info)
    L = datos['laboratorio'][0] if datos['laboratorio'] else "Desconocido"
    P = datos['producto'][0] if datos['producto'] else "Desconocido"

    pd_datos_extraidos["laboratorio"] = L
    pd_datos_extraidos["productos"] = P
    pd_datos_extraidos["fecha_scrapping"] = datetime.date.today()

    # Guardar datos en archivo CSV
    guardar_datos_csv(pd_datos_extraidos, archivo_csv)

#    contador += len(datos['producto'])  # Incrementar el contador con la cantidad de productos scrapeados

#    if contador >= 100:
#        print("Límite de 100 productos alcanzado. Desconectando de Colab...")
#        desconectar_y_reconectar()

#    return pd_datos_extraidos

# Función para simular desconexión y reconexión
#def desconectar_y_reconectar():
 #   print("Guardando estado...")
#    time.sleep(5)
#    print("Desconectando... Por favor, reconecta manualmente y vuelve a ejecutar el script.")
#    os.system("kill -9 $(ps aux | grep '[p]ython' | awk '{print $2}')")
#    exit()

# Scraping de todas las URLs
for url in urls:
    print(f"Scrapeando: {url}")
    try:
        scrap(url)
        time.sleep(random.randint(1, 3))  # Pausa para evitar bloqueos
    except Exception as e:
        print(f"Error al scrapeando {url}: {e}")

import subprocess

# Install Git if not installed
subprocess.run(['sudo', 'apt-get', 'install', '-y', 'git'], check=True)

# Git configuration
subprocess.run(['git', 'config', '--global', 'user.name', 'MartinaZubaran'], check=True)
subprocess.run(['git', 'config', '--global', 'user.email', 'martinazubaran@gmail.com'], check=True)

# Clone the repository (only the first time)
subprocess.run(['git', 'clone', 'https://github.com/MartinaZubaran/Medicamentos.git'], check=True)
subprocess.run(['cd', 'tu_repositorio'], shell=True)

# Move the generated CSV file to the repository folder
subprocess.run(['mv', '/content/productos_scrapeados.csv', './productos_scrapeados.csv'], check=True)

# Commit and push
subprocess.run(['git', 'add', 'productos_scrapeados.csv'], check=True)
subprocess.run(['git', 'commit', '-m', 'Subiendo archivo CSV automáticamente desde Colab'], check=True)
subprocess.run(['git', 'push', 'origin', 'main'], check=True)  # or the branch you are using
