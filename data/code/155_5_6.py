from functools import reduce
import operator

def calculate_sum(numbers):
    return reduce(operator.add, numbers)

if __name__ == '__main__':
    large_integers = [12345678901234567890, 98765432109876543210, 11111111111111111111]
    result = calculate_sum(large_integers)
    print(result)