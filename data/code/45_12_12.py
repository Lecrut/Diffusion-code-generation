def find_min_value(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_values = [3.14, 1.59, 2.65, 3.58, 9.79, 3.23]
    result = find_min_value(sample_values)
    print(result)