def calculate_range(data):
    values = [data[key] for key in data]
    return max(values) - min(values), [key for key in data if data[key] == min(values)][0], [key for key in data if data[key] == max(values)][0]

if __name__ == '__main__':
    sample_data = {
        'A': 10,
        'B': 20,
        'C': 5,
        'D': 30
    }
    range_value, min_label, max_label = calculate_range(sample_data)
    print(f"Range: {range_value}, Min Label: {min_label}, Max Label: {max_label}")