import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


#If no text file is given as a system argument, defaults to nba.txt
if len(sys.argv)<=1:
	filename='nba.txt'
else:
    filename = sys.argv[1]


def getdata(filename,x,y):
    data = pd.read_csv(filename, sep=",", header=0)
    datax = data[['x']]
    datay = data[['y']]
    return (datax,datay,data)

#least squares function using linear algebra to solve for slope, intercept and error.

def leastsquares(filename, x,y): #input data set, explanatory variable, and response variable
    print "\nThe file name is: %s" % filename
    (datax, datay, data)=getdata(filename,x,y)
    data['ones'] = 1
    #print data
    A=data[['ones', 'x']]
    AT=A.transpose()
    b=data[['y']]
    ATA=np.dot(AT, A)
    ATb=np.dot(AT, b)
    xhat=np.linalg.solve(ATA,ATb)
    p=np.dot(A, xhat)
    e=np.subtract(b,p)
    error=np.linalg.norm(e)**2
    print "The least squares regression line is:"
    print "y=%sx+%s" %(xhat[1][0],xhat[0][0])
    print "with error norm %s"  %error
    return (xhat[0][0],xhat[1][0], error) #Returns the intercept, slope, and error.



def graphlsr(filename, x, y):  #input data and two variables, call least squares and then plots the lsr line with the data
    (b,m,error)=leastsquares(filename, x, y)
    (datax, datay, data) = getdata(filename, x, y)
    plt.scatter(datax,datay, color="green")
    plt.plot(datax, b + m * datax)
    plt.title("Least Squares Regression for %s" % filename, fontsize=16)
    datax = datax.as_matrix()
    datay = datay.as_matrix()
    minx=min(datax)
    maxy=max(datay)
    roundb=round(b,2)
    roundm=round(m,2)
    plt.text(minx, maxy, '$y = %0.2f + %0.2f x$' % (b,m))
    plot=plt.show()
    return plot

#Output the slope and intercept of the best-fit line, as well as the sum of the squares
#of the distances from the observed y-values to the y-values on your line.


print graphlsr('population.txt', "x", "y")

print graphlsr('TVlife.txt',"x","y")

#default file is nba.txt
print graphlsr(filename, "x", "y")

print graphlsr('iris.csv',"x","y")






