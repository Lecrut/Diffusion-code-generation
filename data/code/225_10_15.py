def find_min_max(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    minimum = float('inf')
    maximum = float('-inf')
    
    for number in numbers:
        if number < minimum:
            minimum = number
        elif number > maximum:
            maximum = number
    
    return minimum, maximum

if __name__ == '__main__':
    sample_numbers = [15, 3, 88, 42, 9, 71]
    try:
        min_val, max_val = find_min_max(sample_numbers)
        print(f"Minimum value: {min_val}")
        print(f"Maximum value: {max_val}")
    except ValueError as e:
        print(e)