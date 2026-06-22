def validate_numbers(numbers):
    if not isinstance(numbers, list) or len(numbers) != 5:
        raise ValueError("Input must be a list of exactly five numbers")
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise ValueError("All elements in the list must be numbers")

def calculate_sum(numbers):
    validate_numbers(numbers)
    total = sum(numbers)
    return total

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    result = calculate_sum(sample_numbers)
    print(result)