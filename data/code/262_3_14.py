def find_min_max(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    return min(data), max(data)

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "date"]
    min_val, max_val = find_min_max(sample_data)
    print(f"Minimum length string: {min_val}")
    print(f"Maximum length string: {max_val}")