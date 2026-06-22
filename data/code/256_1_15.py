def calculate_range(numbers):
    if not numbers:
        return None
    min_val = max_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return max_val - min_val

if __name__ == '__main__':
    sample_values = (5, 3, 9, 1, 10)
    print(calculate_range(sample_values))