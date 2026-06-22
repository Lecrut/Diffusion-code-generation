def determine_the_largest_number_present_validate(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input must be a list of numbers")
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")
    largest_number = max(numbers)
    return largest_number

if __name__ == '__main__':
    sample_numbers = [15, 25, 35, 45, 55]
    try:
        result = determine_the_largest_number_present_validate(sample_numbers)
        print(result)
    except ValueError as e:
        print(e)