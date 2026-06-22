def calculate_range(numbers):
    if not numbers:
        return 0
    
    min_val = float('inf')
    max_val = -float('inf')
    
    for number in numbers:
        if number < min_val:
            min_val = number
        if number > max_val:
            max_val = number
    
    return max_val - min_val

if __name__ == '__main__':
    sample_list = [10, 5, 20, 3, 15]
    result = calculate_range(sample_list)
    print(result)