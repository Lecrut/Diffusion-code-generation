def find_min_value(numbers):
    if not numbers:
        return None
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_values = [3.5, 1.2, -4.8, 7.6, 0.0]
    print(find_min_value(sample_values))