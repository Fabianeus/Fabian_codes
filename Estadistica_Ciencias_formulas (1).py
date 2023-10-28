#!/usr/bin/env python
# coding: utf-8

# # Promedio 

# In[3]:


def promedio (datos):
    """
    A los datos los sumamos todos (sum) y luego es dividido por su longitud (cantidad)
    """
    
    data = datos
    
    promedio = sum(data) / len(data)
    
    print ("su promedio es:", promedio)
    
    return (promedio)


# # Varianza

# In[2]:


def varianza (promedio):
    """
    Aqui se me olvido agregar que debia tener las dos variables :(
    pero aqui hacemos la resta a todo los valores, potenciamos a dos y luego hacemos la division
    """
    sumatoria_estandar = 0
    
    for v_helio in filtro:
        sumatoria_estandar += (v_helio - promedio)**2
    var = sumatoria_estandar/(len(VHELIO_AVG)-1)
    
    print("La varianza es:", var)
    
    return var


# # Desviacion estandar

# In[3]:


def desv_est (vari):
    """
    Nada del otro mundo, solo sacar el cuadrado
    """
    
    desv_es = (vari)**(1/2)
    
    print ("Y por ende su desviacion estandar es:", desv_es)
    
    return desv_es


# # Rango

# In[7]:


def rango (filtro):
    """
    Buscamos el max y el min, su diferencia es el rango
    """
    rango = max(filtro) - min(filtro)
    print("El rango de los datos", rango)
    


# # Mediana

# In[5]:


def mediana (m):
    """
    El dato que esta en medio, si no encuentra por ser par, entonces toma los dos valores centrales y los promedia
    """
    orden = sorted (m)
    tamaño = len (m)
    
    if tamaño % 2 == 1:
        med = orden[tamaño//2]
    else:
        nucleo = orden[tamaño//2-1]
        nucleosis = orden[tamaño//2]
        med = (nucleo + nucleosis)/2
    print ("la mediana es:")
    return med


# # MAD

# In[5]:


def locura (filtro):
    MEDIANA = mediana (filtro)
    
    rec_mad = []
    
    for fil in filtro:
        dat_mad = abs(fil - MEDIANA)
        rec_mad.append(dat_mad)
    
    li = sorted (rec_mad)
    long = len(rec_mad)
    
    if long % 2 == 1:
        mad = li[long//2]
    else:
        central_1 = li[long // 2-1]
        central_2 = li[long // 2]
        mad = (central_1 + central_2)/2
    print("EL MAD ES:", mad)
    return mad


# # Rango cuartil

# In[12]:


def rango_cuartil(run):
    orden = sorted(run)
    lenght = len(orden)
    
    if lenght % 4 == 0:
        Cuartil_1 = ((orden[lenght // 4 -1] + orden[lenght//4])/2)
        
        Cuartil_3 = (orden[3 * lenght // 4 -1] + orden[3 * lenght // 4])/2
        
        rango_cuartil = Cuartil_3 - Cuartil_1
        
        return rango_cuartil
       
      
    else:
        Cuartil_1 = orden[(lenght + 1) // 4 - 1]
        Cuartil_3 = orden[3 * (lenght + 1) // 4 - 1]
        
        rango_cuartil = Cuartil_3 - Cuartil_1
        
        return rango_cuartil


# # Limites inferiores y superiores

# In[ ]:


def limites (PAT):
    multiplicador = 1.5
    
    orden = sorted(PAT)
    
    lenght = len(orden)
    
    if lenght % 4 == 0:
        Cuartil_1 = ((orden[lenght // 4 -1] + orden[lenght//4])/2)
        
        Cuartil_3 = (orden[3 * length // 4-1] + orden[3* lenght//4])/2
        
        rango_cuartil = Cuartil_3 - Cuartil_1
        
        return rango_cuartil
       
        limite_inferior = Cuartil_1 - multiplicador * rango_cuartil
    
        limite_superior = Cuartil_3 + multiplicador * rango_cuartil
        
        print (limite_superior)
        return limite_superior
        
      
    else:
        Cuartil_1 = orden[(lenght + 1) // 4 - 1]
        Cuartil_3 = orden[3 * (lenght + 1)// 4 - 1]
        
        rango_cuartil = Cuartil_3 - Cuartil_1
        
       
        limite_inferior = Cuartil_1 - multiplicador * rango_cuartil
    
        limite_superior = Cuartil_3 + multiplicador * rango_cuartil   
        
        print ("limite superior:", limite_superior)
        print ("limite inferior:", limite_inferior)
        return limite_superior, limite_inferior


# # Cuartiles

# In[8]:


def cuartiles (datos):
    orden = sorted(datos)
    lenght = len(orden)
    
    if lenght % 4 == 0:
        Cuartil_1 = ((orden[lenght // 4 -1] + orden[lenght//4])/2)
        Cuartil_3 = (orden[3 * lenght // 4-1] + orden[3* lenght//4])/2
        
    
    else:
        Cuartil_1 = orden[(lenght + 1) // 4 - 1]
        Cuartil_3 = orden[3 * (lenght + 1)// 4 - 1]
        
    Cuartiles = (Cuartil_1, Cuartil_3)
    
    print(Cuartiles)
    
    return Cuartiles

