def find_min_value(numbers):
    if not numbers:
        raise ValueError('The list cannot be empty')
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val
if __name__ == '__main__':
    sample_values = [-3, 15, 2, -8, 42]
    try:
        result = find_min_value(sample_values)
        print(result)
    except ValueError as e:
        print(e)