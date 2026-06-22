from operator import gt
from functools import reduce

def find_max(numbers):
    return reduce(lambda x, y: x if gt(x, y) else y, numbers)

if __name__ == '__main__':
    values = [10, 45, 3, 27, 99, 12]
    result = find_max(values)
    print(result)