def calculate_range(data):
    values = data.values()
    range_val = max(values) - min(values)
    min_label = [key for key, value in data.items() if value == min(values)][0]
    max_label = [key for key, value in data.items() if value == max(values)][0]
    return range_val, min_label, max_label

if __name__ == '__main__':
    sample_data = {
        'A': 10,
        'B': 20,
        'C': 5,
        'D': 30
    }
    range_value, min_label, max_label = calculate_range(sample_data)
    print(f"Range: {range_value}, Min Label: {min_label}, Max Label: {max_label}")