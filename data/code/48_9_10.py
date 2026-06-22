from functools import reduce
from operator import or_

def get_max_value(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)

if __name__ == '__main__':
    sample_numbers = [10, 5, 40, 25, 1000, 30, 2]
    result = get_max_value(sample_numbers)
    print(result)