def validate_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numbers")

def sum_large_sequence(numbers):
    validate_numbers(numbers)
    return sum(numbers)

if __name__ == '__main__':
    sample_values = [0.1, 0.2, 0.3, 0.4, 0.5]
    result = sum_large_sequence(sample_values)
    print(result)