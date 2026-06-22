import operator
import functools

def find_max_with_operator(numbers):
    return functools.reduce(operator.max, numbers)

if __name__ == '__main__':
    hard_coded_integers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_max_with_operator(hard_coded_integers)
    print(result)