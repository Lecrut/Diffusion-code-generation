import functools
import operator

def sum_list(numbers):
    return functools.reduce(operator.add, numbers)

if __name__ == '__main__':
    sample_values = [15, 25, 35, 45, 55]
    result = sum_list(sample_values)
    print(result)