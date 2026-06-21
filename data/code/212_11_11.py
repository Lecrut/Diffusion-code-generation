def find_min_max(numbers):
    if not numbers:
        return None, None
    min_val = max_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 7.8, -2.1, 4.6]
    min_val, max_val = find_min_max(sample_values)
    print(f"Minimum: {min_val}, Maximum: {max_val}")