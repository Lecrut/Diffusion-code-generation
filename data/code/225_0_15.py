def find_min_max(numbers):
    if not isinstance(numbers, list) or len(numbers) == 0:
        raise ValueError("Input must be a non-empty list of integers.")
    
    minimum = maximum = numbers[0]
    
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("All elements in the list must be integers.")
        
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    
    return minimum, maximum

if __name__ == '__main__':
    sample_numbers = [15, 3, 88, 42, 9, 76]
    min_val, max_val = find_min_max(sample_numbers)
    print(f"The list of numbers is: {sample_numbers}")
    print(f"The minimum value is: {min_val}")
    print(f"The maximum value is: {max_val}")