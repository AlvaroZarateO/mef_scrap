##############################################################################
######################### PROYECTOS CONSULTA AMIGABLE ########################

import os
import sys
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

##############################################################################
############# GOBIERNO NACIONAL, REGIONAL Y LOCAL (AGREGADOS) ################

# Entrando a ChromeDriver (se puede descargar de https://chromedriver.chromium.org/downloads)
# Antes de eso, chequear bien la versión del Chrome que uno tiene
chromedriver = 'D:/Archivos de Programa/ChromeDriver/chromedriver.exe'
wd = webdriver.Chrome(chromedriver)

# Preparando el bucle: Gobierno Nacional
for k in range(2015, 2021): # En este caso se colocaron los años 2015 - 2020
    wd.get("http://apps5.mineco.gob.pe/transparencia/Navegador/default.aspx")

    # Escogiendo el año en el desplegable (luego hacer bucle por año)
    frame = wd.find_element_by_xpath('//*[@id="frame0"]')
    wd.switch_to.frame(frame)
    
    periodo = Select(wd.find_element_by_xpath("/html/body/form/div[4]/div[2]/table/tbody/tr/td[2]/select[1]"))
    periodo.select_by_value(str(k))
    
    # Para escoger el nivel de gobierno que ejecuta los proyectos: Nacional
    frame = wd.find_element_by_xpath('//*[@id="frame0"]') # Se configura la selección
    wd.switch_to.frame(frame)
    
    niv_gob = wd.find_element_by_name("ctl00$CPH1$BtnTipoGobierno")
    niv_gob.click()
    
    gob_nac = wd.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr[1]")
    gob_nac.click() #Para Gobiernos Locales: /tr[2]. Para Gobiernos Regionales: /tr[3]. Luego, todo es lo mismo
    
    # Seleccionando Función (en este caso: Agropecuaria)
    wd.find_element_by_xpath("//*[@id='ctl00_CPH1_BtnFuncion']").click() # Ordena la tabla en orden alfabético de las funciones
    wd.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[1]/tbody/tr[1]/td[2]").click() # En este caso, al ser "Agropecuaria" la primera función, se coloca tr[1]
    time.sleep(1.5) # No olvidar, sino el código muestra un error (debido a que la página no carga muy rápido)

    funcion = wd.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr[1]/td[1]")
    print(funcion)
    
    # Seleccionando Función Agropecuaria (por orden alfabético)
    funcion.click()
   
    # Seleccionando opción de Departamento
    dptos = wd.find_element_by_name("ctl00$CPH1$BtnDepartamentoMeta")
    dptos.click()
     
    lista_regiones = [3, 5, 6] # En este caso se seleccionaron 3 departamentos: Apurímac, Ayacucho y Cajamarca

    # Preparando bucle para ir por cada departamento
    for i in lista_regiones: 
        region = wd.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr["+ str(i) +"]/td[2]").text
        print(region) # Extrae el texto de la opción y lo muestra en la consola (para orden)
        
        wd.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr["+ str(i) +"]").click()
              
        # Seleccionando Proyectos
        wd.find_element_by_xpath("//*[@id='ctl00_CPH1_BtnProdProy']").click()
        
        # Descargando los archivos de Excel
        d_excel = wd.find_element_by_xpath("/html/body/form/div[4]/div[2]/table/tbody/tr/td[1]/a[2]")
        d_excel.click()
        time.sleep(1.5)
    
        # Volver para cambiar de Departamento
        otro_dep = wd.find_element_by_xpath('//*[@id="ctl00_CPH1_RptHistory_ctl04_TD0"]')
        otro_dep.click()
        time.sleep(1.5)

##############################################################################
###################### GOBIERNOS LOCALES (DESAGREGADO) #######################

# En caso se desee ir por cada gobierno local dentro de cada departamento,
# es mejor probar este código
chromedriver = 'D:/Archivos de Programa/ChromeDriver/chromedriver.exe'
wd = webdriver.Chrome(chromedriver)

# Preparando el bucle: Gobierno Nacional
for k in range(2015, 2021):
    wd.get("http://apps5.mineco.gob.pe/transparencia/Navegador/default.aspx")

    # Escogiendo año en el desplegable (luego hacer bucle por año)
    frame = wd.find_element_by_xpath('//*[@id="frame0"]') # Se configura la selección
    wd.switch_to.frame(frame)
    
    periodo = Select(wd.find_element_by_xpath("/html/body/form/div[4]/div[2]/table/tbody/tr/td[2]/select[1]"))
    periodo.select_by_value(str(k))
    
    # Para escoger el nivel de gobierno: Gobiernos Locales
    frame = wd.find_element_by_xpath('//*[@id="frame0"]')
    wd.switch_to.frame(frame)
    
    niv_gob = wd.find_element_by_name("ctl00$CPH1$BtnTipoGobierno")
    niv_gob.click()
    
    gob_local = wd.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr[2]")
    gob_local.click()
    
    # Seleccionando Función (en este caso: Agropecuaria)
    wd.find_element_by_xpath("//*[@id='ctl00_CPH1_BtnFuncion']").click() # Ordena la tabla en orden alfabético de las funciones
    wd.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[1]/tbody/tr[1]/td[2]").click()
    time.sleep(1.5) # No olvidar, sino el código da error

    # Seleccionando Función Agropecuaria (por orden alfabético)
    funcion = wd.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr[1]/td[1]")
    print(funcion)
    
    # Seleccionando Función Agropecuaria (por orden alfabético)
    funcion.click()
   
    # Seleccionando opción de Departamento
    departamentos = wd.find_element_by_name("ctl00$CPH1$BtnDepartamentoMeta")
    departamentos.click()
     
    lista_regiones = [3, 5, 6] # En este caso se seleccionaron 3 departamentos: Apurímac, Ayacucho y Cajamarca

    # Preparando bucle para ir por cada departamento
    for i in lista_regiones:
        region = wd.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr["+ str(i) +"]/td[2]").text
        print(region) # Extrae el texto de la opción y lo muestra en la consola (para orden)
        
        wd.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr["+ str(i) +"]").click()

        # Como se quieren extraer proyectos de cada gobierno local, se hace esto para bajar de nivel e ir a la sección los mismos
        wd.find_element_by_xpath("//*[@id='ctl00_CPH1_BtnSubTipoGobierno']").click()
        wd.find_element_by_xpath("//*[@id='ctl00_CPH1_RptData_ctl01_TD0']").click() # Sale la opción "Municipalidades" y se selecciona

        # Seleccionando, de nuevo, el departamento en turno (de la lista)
        wd.find_element_by_xpath("//*[@id='ctl00_CPH1_BtnDepartamento']").click()
        wd.find_element_by_xpath("//*[@id='ctl00_CPH1_RptData_ctl01_TD0']").click()
        
        # Desplegando las municipalidades del departamento seleccionado
        wd.find_element_by_xpath("//*[@id='ctl00_CPH1_BtnMunicipalidad']").click()
        
        # Teniendo desplegadas a las municipalidades, lo ideal es ir una por una,
        # y que se descarguen sus proyectos respectivos. Para ello, se hace lo siguiente:
 
        # Se trata de una iteración doble
        
        # Primero, se crea un bucle para contar el número de distritos habidos en el departamento.
        # Para ello, también se crea una función para hacer click en los distritos
        dist = wd.find_elements_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr") # Notar que está incompleto
        time.sleep(1.5)

        cuenta = 1
        
        for dist1 in dist:
            dist1.click()
            
            cuenta = cuenta + 1 # Actualizamos cuenta
        
        # Segundo, habiendo hallado el número, se hace el siguiente bucle:
        for d in range(1, cuenta):
            distrito = wd.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr["+str(d) +"]") # Selecciona cada distritos, pasando en orden, uno por uno
            dist2 = ''.join([j for j in distrito.text if not j.isdigit()])
            dist2 = re.sub('[-:,.]', '', dist2)
            
            print(dist2.strip()) # Indica de qué municipalidad se está descargando en el momento
            distrito.click()
            
            # Seleccionando Proyectos
            wd.find_element_by_xpath("//*[@id='ctl00_CPH1_BtnProdProy']").click()
            time.sleep(1.5)
            
            # Descargando los archivos de Excel
            d_excel = wd.find_element_by_xpath("/html/body/form/div[4]/div[2]/table/tbody/tr/td[1]/a[2]")
            d_excel.click()
            time.sleep(1.5)
        
            # Volver para cambiar de Municipalidad
            otra_muni = wd.find_element_by_xpath('//*[@id="ctl00_CPH1_RptHistory_ctl07_TD0"]')
            otra_muni.click()
            time.sleep(1.5)
           
        # Volver para cambiar de Departamento
        otro_dep = wd.find_element_by_xpath('//*[@id="ctl00_CPH1_RptHistory_ctl04_TD0"]')
        otro_dep.click()
        time.sleep(1.5)
