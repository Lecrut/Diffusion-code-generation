def calculate_range(data):
    if not isinstance(data, dict) or not data:
        raise ValueError("Input must be a non-empty dictionary.")
    
    values = list(data.values())
    min_val = min(values)
    max_val = max(values)
    range_val = max_val - min_val
    
    min_label = [key for key, value in data.items() if value == min_val]
    max_label = [key for key, value in data.items() if value == max_val]
    
    return range_val, min_label[0], max_label[0]

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