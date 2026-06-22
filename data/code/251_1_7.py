def determine_the_largest_number_present_validate(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input must be a list of numbers")
    return max(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    print(determine_the_largest_number_present_validate(sample_numbers))