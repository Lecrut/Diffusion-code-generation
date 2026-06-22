def find_min_max(numbers):
    if not numbers:
        return None, None
    min_num = max_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return min_num, max_num

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 7.8, -2.4, 0.0]
    min_val, max_val = find_min_max(sample_values)
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")