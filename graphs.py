import matplotlib.pyplot as plt
import numpy as np

#Probability for all choosing 1:
x = np.arange(1, 100, 1)
y01 = (1-1/x)**x
ymin=0.5*(2*((x-1)/3)+1)/(3*((x-1)/3)+1)

plt.plot(x, y01,label = "0-1 scheme")
plt.plot(x, ymin,label = "minimum scheme")
plt.xlabel('number of processes - n')
plt.ylabel('Pr(all correct processes decides 1)')
plt.legend()

plt.show()


#Probability for all choosing 0:
x = np.arange(1, 100, 1)
y01 = 1-(1-1/x)**(2*((x-1)/3)+1)
ymin=0.5*(2*((x-1)/3)+1)/(3*((x-1)/3)+1)

plt.plot(x, y01,label = "0-1 scheme")
plt.plot(x, ymin,label = "minimum scheme")
plt.xlabel('number of processes - n')
plt.ylabel('Pr(all correct processes decides 0)')
plt.legend()

plt.show()



#Probability for all choosing same value:
x = np.arange(1, 100, 1)
y01 = (1-(1-1/x)**(2*((x-1)/3)+1))+(1-1/x)**x
ymin=(2*((x-1)/3)+1)/(3*((x-1)/3)+1)

plt.plot(x, y01,label = "0-1 scheme")
plt.plot(x, ymin,label = "minimum scheme")
plt.xlabel('number of processes - n')
plt.ylabel('Pr(all correct processes decides same value)')
plt.legend()

plt.show()


