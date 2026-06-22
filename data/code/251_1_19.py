MAX_NUMBER = float('inf')
MIN_NUMBER = -float('inf')

def validate_input(numbers):
    if not isinstance(numbers, list) or len(numbers) == 0:
        raise ValueError("Input must be a non-empty list")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements in the list must be numbers")

def determine_the_largest_number_present_validate(numbers):
    validate_input(numbers)
    return max(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    result = determine_the_largest_number_present_validate(sample_numbers)
    print(result)