from functools import reduce
import operator

def calculate_sum(numbers):
    return reduce(operator.add, numbers)

if __name__ == '__main__':
    sample_numbers = [12345678901234567890, 98765432109876543210, 11111111111111111111]
    result = calculate_sum(sample_numbers)
    print(result)