def validate_numbers(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
        raise ValueError("Input must be a list of integers")

def find_min_max(numbers):
    validate_numbers(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

if __name__ == '__main__':
    sample_numbers = [15, 3, 88, 42, 9, 76]
    min_val, max_val = find_min_max(sample_numbers)
    print(f"The list of numbers is: {sample_numbers}")
    print(f"The minimum value is: {min_val}")
    print(f"The maximum value is: {max_val}")