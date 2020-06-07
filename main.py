import numpy as np
import matplotlib.pyplot as plt
#Making each thing in the file into separate lists where each elemnt is float.
f = open('Galaxy1 (4).txt','r')
list_make = f.readlines()

All_data = []
Radias  = []
velocity = []
change_in_radias = []
change_in_velocity = []
Mass = []

for line in list_make:
    make_each_list = line.split('\t')
    All_data.append(make_each_list)

for i in All_data:
    Radias.append(i[0])
    velocity.append(i[1])
    change_in_radias.append(i[2])
    change_in_velocity.append(i[3])
    Mass.append(i[4])
    
Radias_Q = (Radias[1:])
velocity_Q = (velocity[1:])
change_in_radias_Q = (change_in_radias[1:])
change_in_velocity_Q = (change_in_velocity[1:])
Mass_data_n_Q = (Mass[1:])

Mass_data_Q = []

for i in Mass_data_n_Q:
    Just_data = i.replace('\n','')
    Mass_data_Q.append(Just_data)

Radias_data = []
velocity_data = []
change_in_radias_data = []
change_in_velocity_data = []
Mass_data = []

for i in Radias_Q:
    Radias_data.append(float(i))

for i in velocity_Q:
    velocity_data.append(float(i))

for i in change_in_radias_Q:
    change_in_radias_data.append(float(i))

for i in change_in_velocity_Q:
    change_in_velocity_data.append(float(i))

for i in Mass_data_Q:
    Mass_data.append(float(i))

# Making arrays for all titles

Radias_data_array = np.array(Radias_data)
velocity_data_array = np.array(velocity_data)
change_in_radias_data_array = np.array(change_in_radias_data)
change_in_velocity_data_array = np.array(change_in_velocity_data)
Mass_data_array = np.array(Mass_data)

# Q.6 

plt.plot(Radias_data_array,velocity_data_array)

plt.xlabel ('Radias / kpc')
plt.ylabel ('velocity / km/s')
plt.title ('Velocity (Blue), Predicted (Orange) Velocity (Visual) Predicted (Green) Velocity (sum) and  as a function of radias')
#plt.show() Since we want to plot 2 lines on same graph with theses axis tis plt.show() needed to be after the other plot is made.

#Q.7 

velocity_predicted_array = np.sqrt(((4.30*10**-6)*Mass_data_array)/Radias_data_array)

#Q.8 

plt.plot(Radias_data_array,velocity_predicted_array)
#plt.show() This is silenced since for week2 we want diffrent graphs.

#Q.9 - Get data from dark matter mass for each radias from Galaxy.txt File

Mass_DM = (4*np.pi*(100*10**6)*(1.87**2))*(Radias_data_array - (1.87*np.arctan(Radias_data_array / 1.87)))

#Q.10 - Graphing visible, dark and their sum matter. Since matter changes with radias we say x = Radias and Mass = y. Also to get DM mass we used radias.
#Reminder from week 1 Radias = distance from planet orbiting mass and centre of orbit. 

#Making mass sum array 

Mass_sum = (Mass_data_array + Mass_DM)

#DM mass plot
#plt.plot(Radias_data_array,Mass_DM)

#plt.xlabel ('Radias / kpc')
#plt.ylabel ('Mass / solar masses')
#plt.title ('Mass of visible, d')

#Visible mass plot
#plt.plot(Radias_data_array,Mass_data_array)

#Sum mass plot

#plt.plot(Radias_data_array,Mass_sum)

#Since plot.show is at the end will show all the plots with the same axis labels on same graph.
#plt.show()

#Q11 -calculate v predicted with Mass_sum and plot it on week 1 graph.
#Since you are plotting on week 1 graph will have to hashtag mass radias plots and unhastag week 1 plots.

#Calculating / making array for v predicted using Mass_sum

velocity_predicted_sum_array = np.sqrt(((4.30*10**-6)*Mass_sum)/Radias_data_array)

#Plotting Mass_sum and v predicted

plt.plot(Radias_data_array,velocity_predicted_sum_array)

plt.show()