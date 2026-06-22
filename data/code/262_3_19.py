def find_min_max_by_length(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    min_elem = max_elem = data[0]
    for x in data:
        if len(x) < len(min_elem):
            min_elem = x
        if len(x) > len(max_elem):
            max_elem = x
    return min_elem, max_elem

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "date"]
    min_val, max_val = find_min_max_by_length(sample_data)
    print(f"Minimum by length: {min_val}")
    print(f"Maximum by length: {max_val}")