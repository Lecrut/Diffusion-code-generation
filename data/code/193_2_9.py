import functools
import operator

def sum_list(numbers):
    return functools.reduce(operator.add, numbers, 0)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(sum_list(sample_values))