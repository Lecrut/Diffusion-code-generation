def find_minimum(numbers):
    if not numbers:
        return None
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_data = [15, -3, 42, 0, -10, 7, 55]
    result = find_minimum(sample_data)
    print(result)