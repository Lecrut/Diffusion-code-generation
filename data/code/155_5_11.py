from functools import reduce
import operator

def sum_large_integers(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    return reduce(operator.add, numbers)

if __name__ == '__main__':
    sample_numbers = [12345678901234567890, 98765432109876543210, 11111111111111111111]
    result = sum_large_integers(sample_numbers)
    print(result)