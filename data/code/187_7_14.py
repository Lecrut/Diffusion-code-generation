def find_max_with_index(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    max_value = numbers[0]
    max_index = 0
    
    for index, value in enumerate(numbers):
        if value > max_value:
            max_value = value
            max_index = index
            
    return (max_value, max_index)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    result = find_max_with_index(sample_numbers)
    print(result)