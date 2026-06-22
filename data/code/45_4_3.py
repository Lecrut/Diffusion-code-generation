def find_min_value(numbers):
    if not numbers:
        raise ValueError("Cannot find minimum of an empty list")
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_data = [45, 12, 89, 3, 67, 21, 99, 4]
    result = find_min_value(sample_data)
    print(result)