def find_minimum(numbers):
    if not numbers:
        return None

    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_data = [34, -50, 42, 14, 55, -10, 99, 0, 23]
    result = find_minimum(sample_data)
    print(result)