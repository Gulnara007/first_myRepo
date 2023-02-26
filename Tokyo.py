import seaborn as sns
import matplotlib.pyplot as plt

x = ['Tokyo','Yokohama','Osaka','Nagoya','Sapporo']
y = [8483050,3579133,2628776,2215031,1880875 ]
sns.barplot(x=x,y=y,color= 'black' )
plt.title('Крупнейшие города Японии')
plt.xlabel('Город')
plt.ylabel('Численность населения в млн.')
plt.show()
