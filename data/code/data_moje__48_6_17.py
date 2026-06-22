import operator
from functools import reduce

def max_value(numbers):
    return reduce(operator.gt, numbers)

if __name__ == '__main__':
    numbers = [10, 45, 23, 89, 12, 67, 34]
    result = max_value(numbers)
    print(result)