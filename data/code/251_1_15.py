def validate_input(data):
    if not isinstance(data, list) or not all(isinstance(num, (int, float)) for num in data):
        raise ValueError("Input must be a list of numbers")
    if len(data) == 0:
        raise ValueError("List cannot be empty")

def determine_the_largest_number_present_validate(numbers):
    validate_input(numbers)
    return max(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    print(determine_the_largest_number_present_validate(sample_numbers))