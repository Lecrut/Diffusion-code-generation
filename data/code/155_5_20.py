from functools import reduce
import operator

def sum_large_integers(numbers):
    return reduce(operator.add, numbers)

if __name__ == '__main__':
    large_numbers = [12345678901234567890, 98765432109876543210, 11111111111111111111]
    result = sum_large_integers(large_numbers)
    print(result)