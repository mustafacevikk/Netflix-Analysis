#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np


# In[4]:


df=pd.read_csv('NetflixOriginals.csv',encoding='latin-1') #UTF-8 hatası aldığımız için kodlamayı "latin-1" olarak değiştirdik.


# In[5]:


df


# In[6]:


df.head()


# In[7]:


df.info()


# In[8]:


data = df.rename(columns={'IMDB Score': 'IMDB'}) #IMDB Score ayrı yazıldığı için IMDB şeklinde düzeltildi.


# In[9]:


data


# In[10]:


data.corr() #korelasyon değerlerine baktığımızda IMDB ile Runtime arasında negatif bir ilişki olduğu görülmekte.


# In[12]:


data.columns #veri setimizdeki başlıkları inceledik.


# In[31]:


data.Runtime.plot(kind = 'line',color = 'yellow',label = 'Runtime',linewidth=2,alpha = 1,grid = True,linestyle = 'dotted')
data.IMDB.plot(color = 'blue',label = 'IMDB',linewidth=2, alpha = 1,grid = True,linestyle = '-.')
plt.legend(loc='upper right')
plt.show() #İzlenme sürelerine göre IMDB'yi inceledik.


# In[43]:


data.IMDB.plot(kind='hist',bins=50,figsize=(9,9),color='blue')
plt.show() #IMDB sayılarını icelediğimizde sıklığın nerede olduğunu görebiliyoruz.


# In[47]:


data.plot(kind='scatter',x='Runtime',y='IMDB',color='yellow')
plt.show() #IMDB vs. Runtime ortak noktalarını incelediğimizde IMDB'nin 6-7 ve RUNTİME'nin 100 olduğu bölümlerde yoğunlaşmanın fazla olduğu görülmektedir.


# In[53]:


filter1=data.IMDB>8 #IMDB'si 8den yüksek olanları inceledik.
data[filter1]


# In[58]:


data[np.logical_and(data['IMDB']>7,data['Genre']=='Animation')] # IMDB'si 7 den yüksek ve türü animasyon olanları inceledik.


# In[63]:


avg=sum(data.IMDB)/len(data.IMDB)
data['quality_level']=['successful' if i>avg else 'unsuccessful' for i in data.IMDB]
data #İMDB sayısı ortalama değerin altındaysa başarısız,üstündeyse başarılı olarak tabloya aktardık.


# In[69]:


data.head 


# In[73]:


print(data['Genre'].value_counts(dropna=False)) #hangi tür diziden ne kadar olduğunu inceledik.


# In[77]:


data2=data.tail()


# In[131]:


data2


# In[105]:


melted=pd.melt(frame=data2,id_vars='Title',value_vars=['Runtime','Premiere']) #df'yi geniş formattan uzun formata istedğimiz şekilde döndürdük.
melted


# In[106]:


import warnings
warnings.filterwarnings("ignore")      #hatayı görmezden gelmesini sağladık.

dh=data.head()
date_list=["2019-08-05","2020-08-21","2019-12-26","2018-01-19","2020-10-30"]
date_object=pd.to_datetime(date_list) #nesne türlü verilerimizi datetime yapıp, verilerimizi tarihsel olarak çekmemizi sağladık.

dh["Date"] = date_object
dh= dh.set_index("Date")
dh


# In[110]:


print(dh.loc["2019-07-21":"2020-11-30"])


# In[111]:


dh.resample("A").mean() #tarih bazında verilerimizin geldiğiğini gördük.


# In[112]:


dh.resample("M").mean() #verilerimizi tarih bazında çağırdığımızda eksik geldiğini görüyoruz.


# In[114]:


dh.resample("M").mean().interpolate("linear") #lineer enterpalasyon yapıp boş verirlerimizi doldurduk.


# In[116]:


data[["Genre","IMDB"]] #dizi türlerine göre imdb'lere bakmak istedim.


# In[119]:


data.loc[1:10,"Genre":"Runtime"]  #türlere göre izlenme sürelerine baktık.


# In[122]:


dataa=data.set_index(["Genre","Title"])
dataa.head(50) #tür ve film adı bazlı tablomuzu getirdik.


# In[130]:


data.groupby("Genre")[["IMDB","Runtime"]].mean() #Son olarakta film türlere göre IMDB-RUNTİME incelediğimizde hangi türden ne kadar izlendiğini ve skoruna bakabiliriz.

