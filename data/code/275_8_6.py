def find_max_min(numbers):
    if not numbers:
        return None, None
    
    max_val = min_val = numbers[0]
    
    for num in numbers:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num
    
    return max_val, min_val

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_max_min(sample_numbers))