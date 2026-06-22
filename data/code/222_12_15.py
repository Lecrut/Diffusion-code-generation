def find_min_value(numbers):
    if not numbers:
        return None
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_data = [7.5, 3.2, 9.8, 1.5, 4.1]
    min_value = find_min_value(sample_data)
    print(min_value)