def calculate_range(data):
    if not all(isinstance(value, (int, float)) for value in data.values()):
        raise ValueError("All values must be integers or floats")
    
    values = list(data.values())
    min_val = min(values)
    max_val = max(values)
    range_val = max_val - min_val
    min_label = [key for key, value in data.items() if value == min_val][0]
    max_label = [key for key, value in data.items() if value == max_val][0]
    
    return range_val, min_label, max_label

if __name__ == '__main__':
    sample_data = {
        'A': 10,
        'B': 20,
        'C': 5,
        'D': 30
    }
    try:
        range_value, min_label, max_label = calculate_range(sample_data)
        print(f"Range: {range_value}, Min Label: {min_label}, Max Label: {max_label}")
    except ValueError as e:
        print(e)