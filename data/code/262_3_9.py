def find_min_max_by_length(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    if not all(isinstance(item, str) for item in data):
        raise ValueError("All elements must be strings")

    minimum = min(data, key=len)
    maximum = max(data, key=len)

    return minimum, maximum

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "date"]
    min_val, max_val = find_min_max_by_length(sample_data)
    print(f"Minimum length string: {min_val}")
    print(f"Maximum length string: {max_val}")

    sample_data_2 = ["short", "longerstring", "medium", "tiny"]
    min_val_2, max_val_2 = find_min_max_by_length(sample_data_2)
    print(f"Minimum length string: {min_val_2}")
    print(f"Maximum length string: {max_val_2}")