import matplotlib.pyplot as plt
temp=[17,20,24,30,32,35,40]
per=[300,200,200,250,240,320,330]
plt.xlabel("Temperature in degree centigrades")
plt.ylabel("Precipitation in centimeters")
plt.scatter(temp,per)
plt.show()