from functools import reduce
import operator

def calculate_list_sum(data):
    return reduce(operator.add, data)

if __name__ == '__main__':
    numbers = [1, 5, 10, 2, 8]
    result = calculate_list_sum(numbers)
    print(result)