import functools
import operator

def sum_integers(integer_list):
    return functools.reduce(operator.add, integer_list)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = sum_integers(sample_values)
    print(result)