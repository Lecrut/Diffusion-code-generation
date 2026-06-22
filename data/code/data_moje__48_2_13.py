def get_max_float(data_points):
    if not data_points:
        raise ValueError("Empty sequence")
    max_val = max(data_points)
    if not isinstance(max_val, float):
        raise TypeError("Non-float value found")
    return max_val

if __name__ == '__main__':
    sample_data = (1.5, 2.3, 0.7, 3.1, 2.9)
    result = get_max_float(sample_data)
    print(result)