def determine_the_largest_number_present_validate(numbers):
    if not isinstance(numbers, list) or len(numbers) == 0:
        raise ValueError("Input must be a non-empty list of numbers")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be numbers")
    return max(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 5, 20, 8, 15]
    largest_number = determine_the_largest_number_present_validate(sample_numbers)
    print(largest_number)