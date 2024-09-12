                        #arithmetic calculator averager#

how_many_number = int(input("enter the how many numbers you have : "))  # we got how many number have.
sum = 0 # we need to learn sum of the numbers.
i = 1 

while i<=how_many_number : 
    numbers = int(input("enter the number : "))
    i = i + 1
    sum = sum + numbers
    averager = sum / how_many_number
print(averager)
    
    