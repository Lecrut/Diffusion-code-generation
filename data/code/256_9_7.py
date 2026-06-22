def calculate_range(data):
    values = data.values()
    if not all(isinstance(v, (int, float)) for v in values):
        raise ValueError("All dictionary values must be integers or floats")
    min_val = min(values)
    max_val = max(values)
    return max_val - min_val

if __name__ == '__main__':
    sample_data = {
        'A': 10,
        'B': 20,
        'C': 5,
        'D': 30
    }
    range_value = calculate_range(sample_data)
    print(f"Range: {range_value}")