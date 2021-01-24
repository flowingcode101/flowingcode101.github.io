from matplotlib import pyplot as plt
import numpy as np
A=plt.subplot(224)
x = np.arange(0,2*np.pi,0.1)   # start,stop,step
y = np.sin(x)
A.plot(x,y,'k')

B=plt.subplot(221)
x = np.arange(0,2.2*np.pi,np.pi/2)   # start,stop,step
y = np.sin(x)
B.plot(x,y,'k.-')

C=plt.subplot(222)
x = np.arange(0,2.2*np.pi,np.pi/4)   # start,stop,step
y = np.sin(x)
C.plot(x,y,'k.-')

C=plt.subplot(223)
x = np.arange(0,2.1*np.pi,np.pi/10)   # start,stop,step
y = np.sin(x)
C.plot(x,y,'k.-')

