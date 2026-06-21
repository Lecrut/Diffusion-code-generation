import functools
import operator

def sum_integers(integer_list):
    return functools.reduce(operator.add, integer_list)

if __name__ == '__main__':
    sample_values = [15, 25, 35, 45, 55]
    print(sum_integers(sample_values))