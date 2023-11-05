print("FIRST COME FIRST SERVE SCHEDULING")
n= int(input("Enter number of processes : "))
d = dict()
for i in range(n):
 key = "P"+str(i+1)
 a = int(input("Enter arrival time of process"+str(i+1)+": "))
 b = int(input("Enter burst time of process"+str(i+1)+": "))
 l = []
 l.append(a)
 l.append(b)
 d[key] = l
d = sorted(d.items(), key=lambda item: item[1][0])
CT = []
for i in range(len(d)):
# first process
 if(i==0):
  CT.append(d[i][1][1])
# get prevCT + newBT
 else:
  CT.append(CT[i-1] + d[i][1][1])
TAT = []
for i in range(len(d)):
 TAT.append(CT[i] - d[i][1][0])
WT = []
for i in range(len(d)):
 WT.append(TAT[i] - d[i][1][1])
avg_WT = 0
for i in WT:
 avg_WT +=i
avg_WT = (avg_WT/n)
avg_TAT = 0
for i in TAT:
 avg_TAT +=i
avg_TAT = (avg_TAT/n)
print("Pno AT BT CT TAT WT")
for i in range(n):
 print(d[i][0]," ",d[i][1][0]," ",d[i][1][1]," ",CT[i]," ",TAT[i]," ",WT[i]," ")
print("Average Waiting Time:%0.2f ms " %(avg_WT))
print("Average Turn Around Time:%0.2f ms " %(avg_TAT))
