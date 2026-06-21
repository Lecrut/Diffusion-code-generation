import functools
import operator

def sum_integers(lst):
    return functools.reduce(operator.add, lst)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(sum_integers(sample_list))