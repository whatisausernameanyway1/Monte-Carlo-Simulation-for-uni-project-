#Monte Carlo Simulation (not a good one)
import random
numeven = 0
ev = 1000000
for i in range(0,ev):
    num = random.randrange(0,10000000)
    if num%2 ==0:
        numeven += 1
result = numeven/ev*100
print(f"{result}% of all Numbers are even.")
