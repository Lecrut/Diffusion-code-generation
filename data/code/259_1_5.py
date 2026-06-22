def find_min_max(numbers):
    min_val = float('inf')
    max_val = float('-inf')
    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    min_value, max_value = find_min_max(sample_values)
    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")