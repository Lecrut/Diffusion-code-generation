def calculate_range(data):
    if not data:
        raise ValueError("Data dictionary is empty")
    
    values = list(data.values())
    min_val = min(values)
    max_val = max(values)
    range_val = max_val - min_val
    
    return range_val, [key for key in data if data[key] == min_val][0], [key for key in data if data[key] == max_val][0]

if __name__ == '__main__':
    sample_data = {
        'A': 10,
        'B': 20,
        'C': 5,
        'D': 30
    }
    range_value, min_label, max_label = calculate_range(sample_data)
    print(f"Range: {range_value}, Min Label: {min_label}, Max Label: {max_label}")