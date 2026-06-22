import operator

def find_max(numbers):
    return reduce(operator.gt, numbers)

from functools import reduce

if __name__ == '__main__':
    values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_max(values))