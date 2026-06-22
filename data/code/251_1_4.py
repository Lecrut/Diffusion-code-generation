def determine_the_largest_number_present_validate(numbers):
    if not isinstance(numbers, list) or len(numbers) == 0:
        raise ValueError("Input must be a non-empty list of numbers")
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements in the list must be numbers")
    
    return max(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    try:
        largest_number = determine_the_largest_number_present_validate(sample_numbers)
        print(largest_number)
    except ValueError as e:
        print(e)