import functools
import operator

def sum_integers(integer_list):
    if not all(isinstance(num, int) for num in integer_list):
        raise ValueError("All elements in the list must be integers")
    return functools.reduce(operator.add, integer_list)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(sum_integers(sample_values))