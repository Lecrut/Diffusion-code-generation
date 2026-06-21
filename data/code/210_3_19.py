def validate_input(numbers):
    if not numbers:
        return None
    for num in numbers:
        if not isinstance(num, (int, float)):
            return None
    return True

def calculate_range(numbers):
    if not validate_input(numbers):
        return None
    minimum = min(numbers)
    maximum = max(numbers)
    return maximum - minimum

if __name__ == '__main__':
    sample_numbers = [10.5, 5.2, 22.8, 8.9, 15.3]
    result = calculate_range(sample_numbers)
    print(result)