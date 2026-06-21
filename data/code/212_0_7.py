def find_min_max(numbers):
    if not numbers:
        return None, None
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

if __name__ == '__main__':
    sample_values = [10, 2, 8, 3, 7]
    min_val, max_val = find_min_max(sample_values)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")

    empty_list = []
    min_val_empty, max_val_empty = find_min_max(empty_list)
    print(f"Empty list Min: {min_val_empty}, Max: {max_val_empty}")