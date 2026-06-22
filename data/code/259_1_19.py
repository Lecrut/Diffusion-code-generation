def find_min_max(numbers):
    min_val = float('inf')
    max_val = float('-inf')
    for number in numbers:
        if number < min_val:
            min_val = number
        if number > max_val:
            max_val = number
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    min_value, max_value = find_min_max(sample_values)
    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")