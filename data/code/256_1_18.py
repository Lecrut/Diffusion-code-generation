def calculate_range(numbers):
    if not numbers:
        raise ValueError("Input tuple must not be empty")
    
    min_val = max_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    
    return max_val - min_val

if __name__ == '__main__':
    sample_tuple = (10, 5, 20, 3, 15)
    try:
        result = calculate_range(sample_tuple)
        print(result)
    except ValueError as e:
        print(e)