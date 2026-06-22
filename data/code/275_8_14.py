def find_max_min(numbers):
    if not numbers:
        return None, None
    
    max_val = min_val = numbers[0]
    
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num
    
    return max_val, min_val

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, -2, 7]
    
    if not all(isinstance(num, (int, float)) for num in sample_numbers):
        print("Error: List contains non-numeric values.")
    else:
        max_value, min_value = find_max_min(sample_numbers)
        print(f"Max: {max_value}, Min: {min_value}")