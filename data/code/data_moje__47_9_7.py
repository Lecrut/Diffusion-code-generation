from functools import reduce
from operator import add

def calculate_mean(numbers):
    return reduce(add, map(float, numbers)) / len(numbers)

if __name__ == '__main__':
    values = [1.5, 2.5, 3.5, 4.5, 5.5]
    print(calculate_mean(values))