from functools import reduce

def validate_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numbers")
    return numbers

def sum_numbers(numbers):
    validated_numbers = validate_numbers(numbers)
    return reduce(lambda x, y: x + y, validated_numbers)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    result = sum_numbers(sample_values)
    print(result)