def fibbonaci():
	a = 0
	b = 1
	sum = 0
	x = int(input("enter sequence end: \n"))
	print(a,end=" ")
	print(b,end=" ")
	for i in range(2,x):
		sum = a + b
		a = b
		b = sum
		print (sum,end=' ')
	print()


fibbonaci()
		
 
