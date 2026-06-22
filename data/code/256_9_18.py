def calculate_range(data):
    values = data.values()
    min_val = min(values)
    max_val = max(values)
    range_val = max_val - min_val
    min_label = [key for key, value in data.items() if value == min_val][0]
    max_label = [key for key, value in data.items() if value == max_val][0]
    return range_val, min_label, max_label

if __name__ == '__main__':
    sample_data = {
        'X': 15,
        'Y': 25,
        'Z': 5,
        'W': 35
    }
    range_value, min_label, max_label = calculate_range(sample_data)
    print(f"Range: {range_value}, Min Label: {min_label}, Max Label: {max_label}")