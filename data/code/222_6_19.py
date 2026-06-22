def find_minimum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    min_value = numbers[0]
    for num in numbers[1:]:
        if num < min_value:
            min_value = num
    
    return min_value

if __name__ == '__main__':
    sample_list = [10, 3.14, 5, -2.5, 100, "a", 0]
    try:
        result = find_minimum(sample_list)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")