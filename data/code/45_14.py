def get_minimum(numbers: list) -> float:
    if not numbers:
        raise ValueError("List must not be empty")
    
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_values = [34, 15, 88, 2, 67, 19, 90, 5]
    result = get_minimum(sample_values)
    print(result)