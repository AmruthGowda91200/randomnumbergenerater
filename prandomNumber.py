import random

def roll() : 
    min_value = 1
    max_value = 100
    roll = random.randint(min_value,max_value)

    return roll

value = roll()
print(value)
