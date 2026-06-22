def calculate_range(data):
    values = data.values()
    min_value = min(values)
    max_value = max(values)
    return f"Range: {max_value - min_value}"

if __name__ == '__main__':
    sample_data = {
        'A': 10,
        'B': 20,
        'C': 5
    }
    print(calculate_range(sample_data))