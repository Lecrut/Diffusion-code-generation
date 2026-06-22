def validate_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numbers")
    if len(numbers) != 5:
        raise ValueError("There must be exactly five numbers")

def calculate_sum(numbers):
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    validate_numbers(sample_numbers)
    result = calculate_sum(sample_numbers)
    print(result)