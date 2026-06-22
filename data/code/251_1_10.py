def determine_the_largest_number_present_validate(numbers):
    if not isinstance(numbers, list) or len(numbers) == 0:
        raise ValueError("Input must be a non-empty list of numbers")
    
    max_value = float('-inf')
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements in the list must be numbers")
        if num > max_value:
            max_value = num
    
    return max_value

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    print(determine_the_largest_number_present_validate(sample_numbers))