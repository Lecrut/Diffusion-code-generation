from functools import reduce
import operator

def validate_input(data):
    if not all(isinstance(x, int) for x in data):
        raise ValueError("All elements must be integers")

def sum_large_integers(numbers):
    validate_input(numbers)
    return reduce(operator.add, numbers)

if __name__ == '__main__':
    sample_numbers = [12345678901234567890, 98765432109876543210, 11111111111111111111]
    result = sum_large_integers(sample_numbers)
    print(result)