def calculate_range(numbers):
    if not numbers:
        return 0
    
    min_val = float('inf')
    max_val = float('-inf')
    
    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return max_val - min_val

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    result = calculate_range(sample_list)
    print(result)