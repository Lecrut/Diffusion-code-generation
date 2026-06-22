def find_minimum(numbers):
    if not numbers:
        raise ValueError("List must be non-empty")
    
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [34, -50, 42, 14, -5, 0, 99, -12]
    result = find_minimum(sample_list)
    print(result)