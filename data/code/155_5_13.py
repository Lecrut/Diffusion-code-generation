from functools import reduce
import operator

def validate_input(data):
    if not all(isinstance(item, int) for item in data):
        raise ValueError("All elements in the list must be integers.")
    return data

def sum_large_integers(numbers):
    validated_numbers = validate_input(numbers)
    total_sum = reduce(operator.add, validated_numbers)
    return total_sum

if __name__ == '__main__':
    sample_numbers = [12345678901234567890, 98765432109876543210, 11111111111111111111]
    result = sum_large_integers(sample_numbers)
    print(result)