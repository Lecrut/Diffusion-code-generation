def find_min_max(numbers):
    min_val = min(numbers)
    max_val = max(numbers)
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [34, 12, 90, 56, 78]
    min_value, max_value = find_min_max(sample_values)
    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")