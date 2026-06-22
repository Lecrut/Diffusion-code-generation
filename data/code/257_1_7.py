def calculate_extremes_difference(numbers):
    if not numbers:
        raise ValueError("The tuple must contain at least one number.")
    
    max_number = float('-inf')
    min_number = float('inf')
    
    for num in numbers:
        if num > max_number:
            max_number = num
        if num < min_number:
            min_number = num
    
    return max_number - min_number

if __name__ == '__main__':
    sample_values = (7.8, 2.3, 9.1, 4.5)
    print(calculate_extremes_difference(sample_values))