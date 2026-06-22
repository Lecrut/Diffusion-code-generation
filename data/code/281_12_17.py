def validate_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numbers")
    if len(numbers) != 5:
        raise ValueError("Exactly five numbers are required")

def calculate_sum(*numbers):
    validate_numbers(numbers)
    return sum(numbers)

if __name__ == '__main__':
    sample_values = (1.5, 2.5, 3.5, 4.5, 5.5)
    result = calculate_sum(*sample_values)
    print(result)