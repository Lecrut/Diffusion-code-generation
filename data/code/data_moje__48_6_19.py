from operator import gt
from functools import reduce

def find_max(values):
    return reduce(lambda a, b: a if gt(a, b) else b, values)

if __name__ == '__main__':
    numbers = [10, 45, 3, 100, 22, 7]
    result = find_max(numbers)
    print(result)