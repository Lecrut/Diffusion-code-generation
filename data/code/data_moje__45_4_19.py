def find_minimum(numbers):
    if not numbers:
        raise ValueError("Cannot find minimum of an empty list")
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_data = [34, 12, 56, 8, 99, 2, 45, 1]
    result = find_minimum(sample_data)
    print(result)