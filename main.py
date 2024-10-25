import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



x=[1,2,4,5,6,8,9]
y=[2,4,6,8,9,15,18]
'''
plt.plot(x,y) #light blue line connect dots
plt.show()


plt.plot(x,y,"ro") #red dots
plt.show()


plt.plot(x,y,"g^") #green traingles
plt.show()


plt.plot(x,y,"r--") #red dasehd line
plt.show()


plt.plot(x,y,"b--") #blue dashed line
plt.show()


plt.plot(x,y,"b-") #solid blue line
plt.show()



plt.plot(x,y,"r--",label="Y=X+2")

plt.axis([0,10,0,19])#range

plt.xlabel("X")
plt.ylabel("Y")
plt.title("XY graph")
plt.legend()
plt.show()
'''
plt.figure(figsize=(12,7))
x=np.arange(0,5,0.5)

y1=5*x+2
plt.plot(x,y1,label="Y=5X+2")

y2=x**2
plt.plot(x,y2,"r--",label="Y=X^2")

y3=x**3
plt.plot(x,y3,"b--",label="Y=X^3")



plt.xlabel("X")
plt.ylabel("Y")
plt.title("XY graph")
plt.grid(True)

plt.axhline(0,color="black",linewidth=2)
plt.axvline(0,color="black",linewidth=2)


plt.legend()
plt.show()



#bar graph

plt.bar(["Male","Females"],[7,13],color='b')
plt.bar(["Male","Females"],[7,13],color='g')
plt.show()




#### HISTOGRAMS #####

ages = [22,55,36,45,21,67,45,23,89,11,33,67,88,67,89,12,6,9,48,68,18]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages,bins,histtype="bar",rwidth=0.8)
plt.xlabel("Ages")
plt.ylabel("Amount")
plt.title("Histogram")
plt.show()



x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6]) #
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])


plt.scatter(x,y,label="Age vs Speed",color="Black",s=50)
plt.xlabel("Ages")
plt.ylabel("SPeed")
plt.title("Cataplot")
plt.show()

