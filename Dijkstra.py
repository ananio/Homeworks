#Main
from graph import Graph
import time

import sys

def retList(array):
	list = []
	for i in array:
		i = i.replace("\n", "")
		k = 0
		aux = 0
		test = i.split("\t")

		for j in test:
			
			if(k==0):
				k = 1
				aux = int(j)
				continue
			try:
				list.append([int(aux), (int(j.split(",")[0]), int(j.split(",")[1]))])
			except:
				jota = 0
				
	return list
	
if __name__ == "__main__":
	text_file = open("dijkstraData-test.txt", "r")
	#text_file = open("test1.txt", "r")
	#text_file = open("test2.txt", "r")
	#text_file = open("test3.txt", "r")
	#text_file = open("test4.txt", "r")
	#text_file = open("test5.txt", "r")

	array = text_file.readlines()	
	list_array = retList(array)
	
	#print list_array
	
	graphs = Graph(list_array)
	graphs.printable()