def find_min_max(data):
    if not data:
        raise ValueError("Input dictionary cannot be empty")
    minimum = min(data.values())
    maximum = max(data.values())
    return minimum, maximum

if __name__ == '__main__':
    sample_dict = {1: 3, 2: 1, 3: 4, 4: 1, 5: 5, 6: 9, 7: 2, 8: 8}
    min_val, max_val = find_min_max(sample_dict)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")