import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv
df=pd.read_csv("C:/Users/dell/Desktop/Python/folderA/datas/medium_data.csv")
data=df["reading_time"].tolist()
def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return(mean)
meanList=[]
for i in range(0,1000):
    setOfMean=randomSetOfMean(100)
    meanList.append(setOfMean)
mean=statistics.mean(data)
stddev=statistics.stdev(data)
print(mean)
print(stddev)
fsss,fsse=mean-stddev,mean+stddev
ssss,ssse=mean-(2*stddev),mean+(2*stddev)
tsss,tsse=mean-(2*stddev),mean+(2*stddev)
fig=ff.create_distplot([meanList],["studentMarks"],show_hist=False)
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
#fig.add_trace(go.Scatter(x=[fsss,fsss],y=[0,0.17],mode="lines",name="fsss"))
#fig.add_trace(go.Scatter(x=[ssss,ssss],y=[0,0.17],mode="lines",name="ssse"))
#fig.add_trace(go.Scatter(x=[tsss,tsss],y=[0,0.17],mode="lines",name="ssse"))
df=pd.read_csv("C:/Users/dell/Desktop/Python/sample_1.csv")
data=df["reading_time"].tolist()
meanOfSample2=statistics.mean(data)
print(meanOfSample2)
fig.add_trace(go.Scatter(x=[meanOfSample2,meanOfSample2],y=[0,0.17],mode="lines",name=(meanOfSample2)))
df=pd.read_csv("C:/Users/dell/Desktop/Python/sample_2.csv")
data=df["reading_time"].tolist()
meanOfSample3=statistics.mean(data)
print(meanOfSample3)
fig.add_trace(go.Scatter(x=[meanOfSample3,meanOfSample3],y=[0,0.17],mode="lines",name=(meanOfSample3)))
df=pd.read_csv("C:/Users/dell/Desktop/Python/sample_3.csv")
data=df["reading_time"].tolist()
meanOfSample1=statistics.mean(data)
print(meanOfSample1)
fig.add_trace(go.Scatter(x=[meanOfSample1,meanOfSample1],y=[0,0.17],mode="lines",name=(meanOfSample1)))
zscore1=(mean-meanOfSample1)/stddev
zscore2=(mean-meanOfSample2)/stddev
zscore3=(mean-meanOfSample3)/stddev
print(zscore1)
