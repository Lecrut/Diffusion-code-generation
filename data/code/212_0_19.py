def find_min_max(data):
    if not data:
        return None, None
    minimum = min(data)
    maximum = max(data)
    return minimum, maximum

if __name__ == '__main__':
    sample_values = [7, 3, 9, 2, 5]
    min_val, max_val = find_min_max(sample_values)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")