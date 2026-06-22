def validate_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numbers")

def calculate_sum_and_round(numbers):
    validate_numbers(numbers)
    total = sum(numbers)
    return round(total, 2)

if __name__ == '__main__':
    sample_values = [1.2345, 6.7890, 2.3456, 3.4567]
    result = calculate_sum_and_round(sample_values)
    print(result)