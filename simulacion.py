#!/bin/python
from random import random
def Ll1():
	ll1 = [3,4,4,5,5,5,6]
	i = int(7*random())
	return ll1[i]

def Ll2():
	ll1 = [3,4,4,4,5]
	i = int(5*random())
	return ll1[i]

def V1():
	ll1 = [3,4,4,4,4,5,5,5,6]
	i = int(9*random())
	return ll1[i]

def V2():
	ll1 = [3,3,3,4,4,4,5,5]
	i = int(8*random())
	return ll1[i]

def media(x):
	suma = sum(x)
	return float(suma)/float(len(x))

def var(x):
	suma2 = 0
	for i in range(0,len(x)):
		suma2 = suma2 + x[i]**2
	return float(float(suma2 - media(x)**2)/len(x))

f = open("resultados.txt","w")
#el valor maximo de la represa R1 es 4 y de la represa R2 es 6
line = "R1" + "\t\t" + "R2" + "\t\t" + "Ll1" + "\t\t" + "Ll2" + "\t\t"  + "V1" + "\t\t" + "V2" + "\t\t" + "T12" + "\t\t" + "e1" + "\t\t" + "e2" + "\t\t" + "AM\n"
f.writelines(line)
a = {"R1":0, "R2":0, "T12":0,"e1":0,"e2":0,"AM":0} #los datos de la represas, transferencia y error
l1 = []
l2 = []
total_it = 80000
for x in range(1,40):
	se1 = 0
	se2 = 0
	sv1 = 0
	sv2 = 0
	d = 0
	while d < total_it:
		ll1 = Ll1()
	 	ll2 = Ll2()
		v1 = V1()
		v2 = V2()
		a["e1"] = 0
		a["e2"] = 0
		a["T12"] = 0
		a["AM"] = 0
		line = str(a["R1"]) + "\t\t" + str(a["R2"]) + "\t\t" + str(ll1) + "\t\t" + str(ll2) + "\t\t" + str(v1) + "\t\t" + str(v2)
		f.writelines(line)
		if ll1 > v1:
			if (ll1 - v1 + a["R1"]) <= 4:
				a["R1"] = a["R1"] + ll1 - v1
			else:
				a["T12"] = ll1 - v1 - 4 + a["R1"]
				a["R1"] = 4
		elif ll1 < v1:
			if a["R1"] >= (v1 - ll1):
				a["R1"] = a["R1"] - v1 + ll1
			else:
				a["e1"] = v1 - ll1 - a["R1"]
				a["R1"] = 0
		if a["T12"] + a["R2"] > 6:
			a["AM"] = a["T12"] + a["R2"] - 6
		else:
			a["R2"] = a["R2"] + a["T12"]
		if ll2 > v2:
			if(ll2 - v2 + a["R2"]) <= 6:
				a["R2"] = a["R2"] + ll2 - v2
			else:
				a["AM"] = a["AM"] + ll2 - v2 -6 + a["R2"]
				a["R2"] = 6
		elif ll2 < v2:
			if a["R2"] >= (v2 - ll2):
				a["R2"] = a["R2"] - v2 + ll2
			else:
				if a["R1"] > 2:
					if (v2 - ll2) <= (a["R1"] - 2):
						a["R1"] = a["R1"] - v2 + ll2
					else:
						a["e2"] = v2 - ll2 - a["R1"] + 2
				else:
					a["e2"] = v2 - ll2 - a["R2"]	
					a["r2"] = 0
	
		se1 = se1 + float(a["e1"])
		se2 = se2 + float(a["e2"])
		sv1 = sv1 + float(v1)
		sv2 = sv2 + float(v2)
		line = "\t\t" + str(a["T12"]) + "\t\t" + str(a["e1"]) + "\t\t" + str(a["e2"]) + "\t\t" + str(a["AM"]) + "\n"
		f.writelines(line)
		d = d + 1
	print str(se1/sv1),str(se2/sv2)
	l1.append(se1/sv1)
	l2.append(se2/sv2)
print var(l1)
print var(l2)
f.close
