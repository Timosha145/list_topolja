#uezdi=['Tallinn','Narva, Narva-Jõesuu','Kohtla-Järve','Ida-Virumaa, Lääne-Virumaa, Jõgevamaa','Tartu linn','Tartumaa, Põlvamaa, Võrumaa, Valgamaa','Viljandimaa, Järvamaa, Harjumaa, Raplamaa','Pärnumaa','Läänemaa, Hiiumaa, Saaremaa']
#while 1:
#	try:
#		indeks=int(input('Введи свой почтовый индекс: '))
#		if indeks>=10000 and indeks<=99999:
#			break
#	except ValueError:
#		print('Не существует такого индекса')
#indeks=indeks//10000-1
#print(uezdi[indeks-1])
#if indeks in [0,1,2]:
#	print('Не вылезай из дома!')1


#from random import *
#a=randint(2,8)
#list=[]
#for i in range (a):
#	list.append(randint(0,9))
#print(list)
#print()
#n=int(input('Сколько раз перевернуть: '))
#v1=list[0]
#v2=len(list)
#for i in range (n):
#	vv1=list[v1]
#	list.insert(v1,list[v2])
#	list.pop(1)
#	list.insert(v2,vv1)
#	list.pop(len(list)-1)
#	v1=+v1
#	v2=-v2
#print(list)

#from random import *
#n=randint(5,30)
#list=[]
#maxA=0
#for i in range (n):
#	a=randint(0,100)
#	if a>maxA:
#		maxA=a
#	list.insert(0,a)
#maxA=round(maxA/len(list),2)
#print(list)
#print('Самое большое из них, а затем делённое на длину списка - ',maxA)

#from random import *
#n=randint(10,50)
#b=0
#list=[]
#for i in range (n):
#	a=randint(-100,100)
#	list.insert(0,a)
#print(list)
#v=int(input('Сортировать по убыванию(0)/возрастанию(1)?: '))
#for i in range (n):
#	list.insert(0,abs(list[b]))
#	b+=1
#	list.pop(b)
#if v==1:
#	list.sort()
#else: 
#	list.sort(reverse=True)
#print(list)