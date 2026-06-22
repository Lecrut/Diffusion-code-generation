def extract_max_float(data_points):
    if not data_points:
        raise ValueError("Empty sequence")
    max_val = None
    for item in data_points:
        if not isinstance(item, float):
            continue
        if max_val is None or item > max_val:
            max_val = item
    if max_val is None:
        raise TypeError("No float values found")
    return max_val

if __name__ == '__main__':
    sample_data = (3.14, 2.71, 1.41, 9.8, 5.5)
    result = extract_max_float(sample_data)
    print(result)