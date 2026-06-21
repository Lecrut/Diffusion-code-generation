import functools
import operator

def sum_integers(integer_list):
    return functools.reduce(operator.add, integer_list, 0)

if __name__ == '__main__':
    sample_values = [15, -5, 30, -20]
    print(sum_integers(sample_values))