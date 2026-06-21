from functools import reduce
import operator

def sum_large_integers(numbers):
    return reduce(operator.add, numbers)

if __name__ == '__main__':
    sample_numbers = [12345678901234567890] * 1000
    print(sum_large_integers(sample_numbers))