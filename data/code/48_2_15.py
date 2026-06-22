def extract_max_float(data_points):
    if not data_points:
        raise ValueError("Empty sequence provided")
    max_val = None
    for item in data_points:
        if not isinstance(item, float):
            raise TypeError(f"Expected float, got {type(item).__name__}")
        if max_val is None or item > max_val:
            max_val = item
    return max_val

if __name__ == '__main__':
    sample_data = (1.5, 3.7, 2.2, 4.9, 0.1)
    result = extract_max_float(sample_data)
    print(result)