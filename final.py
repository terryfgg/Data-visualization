import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#匯入資料
filename = 'data.csv'
df = pd.read_csv(filename)

#以欄位整理資料
ege = df['年份']   #年份 97 to 107
sys_mem = df['國父紀念館']
cks_mem = df['國立中正紀念堂']
palace = df['國立故宮博物院']
taipei_zoo = df['市立動物園']
fishermman = df['淡水漁人碼頭']
shilin_park = df['士林官邸公園']
tallest = df['台北101景觀台']


#折線圖
'''
x = ege
y1 = sys_mem
y2 = cks_mem
y3 = palace
y4 = taipei_zoo
y5 = fishermman
y6 = shilin_park
y7 = tallest
plt.plot(x, y2, label= 'CKS_MEM', color = "blue")
plt.plot(x, y1, label= 'SYS_MEM', color= "gray")
plt.plot(x, y3, label= 'National_palace', color = "red")
plt.plot(x, y4, label= 'Taipei_zoo', color = "black")
plt.plot(x, y5, label= 'Fisherman_Wharf', color = "purple")
plt.plot(x, y6, label= 'Shilin_Park',color = "green")
plt.plot(x, y7, label= 'Taipei_101', color = "pink")
plt.title("Taipei Trip Destination Stat")
plt.xlabel("Years")
plt.ylabel("visited")
plt.legend()
plt.show()
'''


#長條圖
'''
x = ege
y1 = sys_mem
y2 = cks_mem
y3 = palace
y4 = taipei_zoo
y5 = fishermman
y6 = shilin_park
y7 = tallest
plt.bar(x, y1, label='SYS_MEM', align = "edge", width=0.35)
plt.bar(x, y2, label='CKS_MEM',align = "edge", width=-0.35)
plt.bar(x, y3, label='Palace', align = "edge", width=-0.30)
plt.bar(x, y4, label='Taipei_zoo',align = "edge", width=0.30)
plt.bar(x, y5, label='Fisherman_Wharf', align = "edge", width=0.40)
plt.bar(x, y6, label='Shilin_park', align = "edge", width=-0.4)
plt.bar(x, y7, label='Taipei_101', align = "edge", width=-0.25)
plt.title("Taipei Trip Destination Stat")
plt.xlabel("Years")
plt.ylabel("visited")
plt.legend()
plt.show()
'''

#圓餅圖
'''
x = ege
y1 = sys_mem.sum()
y2 = cks_mem.sum()
y3 = palace.sum()
y4 = taipei_zoo.sum()
y5 = fishermman.sum()
y6 = shilin_park.sum()
y7 = tallest.sum()
total_compara = [y1, y2, y3, y4, y5, y6, y7]
place = ['SYS_MEM', 'CKS_MEM', 'National_Palace', 'Taipei_Zoo', 'Fisherman_Wharf', 'shilin_offical_park', 'taipei_101']
colors = ["lightgreen", "lightblue", "yellow", "pink", 'purple', 'blue', 'brown']
plt.pie(total_compara,labels = place,                
        autopct = "%1.1f%%",                       
        pctdistance = 0.6,              
        textprops = {"fontsize" : 12},  
        shadow=True)
plt.axis("equal")
plt.title('Taipei Trip Destination Comparison in last ten years'), {'fontsize ': 18}
plt.legend(loc = 'best')
plt.show()
'''



#統計資訊 平均數 變動數 標準差
print(df.mean())
print(df.var())
print(df.std())
print(df.describe())
