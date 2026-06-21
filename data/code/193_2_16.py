import functools
import operator

def sum_integers(integer_list):
    return functools.reduce(operator.add, integer_list)

if __name__ == '__main__':
    sample_values = [100, 200, 300]
    result = sum_integers(sample_values)
    print(result)