def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list must not be empty")
    
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_data = [34, 15, 88, 2, 99, 3, 101, 27]
    result = find_minimum(sample_data)
    print(result)