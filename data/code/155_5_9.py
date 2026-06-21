from functools import reduce
import operator

def validate_input(data):
    if not isinstance(data, list) or not all(isinstance(x, int) for x in data):
        raise ValueError("Input must be a list of integers")

def calculate_list_sum(data):
    validate_input(data)
    return reduce(operator.add, data)

if __name__ == '__main__':
    sample_numbers = [12345678901234567890, 98765432109876543210, 11111111111111111111]
    result = calculate_list_sum(sample_numbers)
    print(result)