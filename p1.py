sum1 = 0 #sum of all numbers<1000 divisible by 3
sum2 = 0 #sum of all numbers <1000 divisible by 5
sum3 = 0 #sum of all numbers <1000 divisible by 15

i = 3
j = 5
k = 15
while i<1000: #slowest pointer
	sum1+=i
	i+=3
	if j<1000:
		sum2+=j
		j+=5
	if k <1000:
		sum3+=k
		k+=15
print(sum1+sum2-sum3) #excluding the double count