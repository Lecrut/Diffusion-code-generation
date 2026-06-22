def calculate_range(data):
    values = data.values()
    min_val = min(values)
    max_val = max(values)
    return max_val - min_val, list(data.keys())[list(data.values()).index(min_val)], list(data.keys())[list(data.values()).index(max_val)]

if __name__ == '__main__':
    sample_data = {
        'X': 10,
        'Y': 25,
        'Z': 5
    }
    range_value, min_label, max_label = calculate_range(sample_data)
    print(f"Range: {range_value}, Min Label: {min_label}, Max Label: {max_label}")