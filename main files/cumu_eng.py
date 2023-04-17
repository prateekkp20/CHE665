import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.figure(figsize=(15,10))

data1 = np.loadtxt('ntote.txt')

x = data1[:, 0]
y = data1[:, 1]
line1, =plt.plot(x, y,'r')


df_data = pd.read_csv('ntot.txt')

df_data1 = pd.DataFrame(df_data)

#print (df_data1)

df_data1['CA'] = df_data1.expanding().mean()

#df_data['CA'] = df_data1.expanding().mean()


line2, =plt.plot(df_data1['CA'], linewidth=2, color='b')

df_data1['CA'].to_csv (r'./te.txt', index = False, header=False)
#print (df_data2)
#df.stack(df_data['CA']).std()
#my_df = pd.DataFrame(df_data2)
data = np.loadtxt('te.txt')
#data1 = np.array([data])
#print (data1)
#print (data)
#print (my_df)
#print(df_data2['1'].mean())
#print(my_df['1'].std())
#x=list(var['time'])
#data2 = np.array([7,5,4,9,12,45])
#print(data2)
#y1=list(var['totalenergy'])

def mean(data):
  n = len(data)
  mean = sum(data) / n
  return mean

def variance(data):
  n = len(data)
  mean = sum(data) / n
  deviations = [(x - mean)**2 for x in data]
  variance = sum(deviations) / n
  return variance

def stdev(data):
  import math
  var = variance(data)
  std_dev = math.sqrt(var)
  return std_dev

print("Variance is % s "% (variance(data)))
print("Standard Deviation is % s "% (stdev(data)))
print("Mean is % s " % (mean(data)))

n = len(data)
print(n)

#print (df_data1['CA'])


#x=list(var['time'])

#y1=list(var['totalenergy'])

#y2=list(var['fi data'])

#line1, =plt.plot(x,y1,color='red',linewidth=1)#'r:o',markersize=4.7, linewidth=2)

#line2, =plt.plot(x,y2,'ro',markersize=8)

#def func(x, a, b):
#     return a * x + b

#params =curve_fit(func, x, y)
#[a, b] = params[0]

#print('y = %.5f * x + %.5f' % (a, b))

ax = plt.subplot()
ax.plot()
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines["left"].set_linewidth(2)
ax.tick_params(axis="y", length=6, width=2)
ax.tick_params(axis="x", length=6, width=2)

s1=20
s2=15
s3=25

#ax.text(0.042, 0.9568, '1273K', fontsize=s1)

plt.yticks(fontsize=s2,fontweight='bold')
plt.xticks(fontsize=s2,fontweight='bold')
#plt.ticklabel_format(axis="y", style="sci")
plt.grid(b=True, which='both', color='0.65', linestyle='-')
ax.ticklabel_format(useOffset=False)
#ax.ticklabel_format(style='plain')
#plt.minorticks_on()
#ax = sinplot()
# Show the major grid and style it slightly.
#ax.grid(which='major', color='#DDDDDD', linewidth=0.8)
# Show the minor grid as well. Style it in very light gray as a thin,
# dotted line.
#ax.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=0.5)
# Make the minor ticks and gridlines show.
#ax.minorticks_on()

plt.xlabel("Time (fs)", fontsize=s3,fontweight='bold')   #Time (fs)
plt.ylabel("Total energy (eV)", fontsize=s3,fontweight='bold')
#plt.ylim(0.9495, 0.9578)
#plt.xlim(0, 260)
#plt.arrow(x=73, y=5, dx=-13, dy=-4,width=.9,fc="k", ec="k",head_width=2.7, head_length=2.5)
#plt.text(75,4,'Selected configuration',fontsize=12,fontweight='bold')
#plt.axhline(y=20, color='b', linestyle='--')#, linewidth=3.5)

#plt.rcParams["axes.edgecolor"] = "0.45"
#plt.rcParams["axes.linewidth"]  = 3.45
#plt.margins(0.125)
#plt.legend(loc='upper left')

plt.legend((line1,line2),('Kinetic+Potential','Cumulative average'),loc='best',fontsize=s1)
#plt.tight_layout()
plt.savefig('total_energy', dpi=160)#, bbox_inches='tight')
plt.show()







