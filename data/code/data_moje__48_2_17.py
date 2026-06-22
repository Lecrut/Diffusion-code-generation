def extract_max_float(data_points):
    if not data_points:
        raise ValueError("Sequence cannot be empty")
    max_val = float('-inf')
    found_float = False
    for value in data_points:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Invalid type {type(value)} for value {value}")
        float_val = float(value)
        if float_val > max_val:
            max_val = float_val
        found_float = True
    if not found_float:
        raise ValueError("No valid numeric values found")
    return max_val

if __name__ == '__main__':
    sample_data = (3.5, 2.1, 9.8, 4.0, 7.2)
    result = extract_max_float(sample_data)
    print(result)
    empty_data = ()
    try:
        extract_max_float(empty_data)
    except ValueError as e:
        print(str(e))