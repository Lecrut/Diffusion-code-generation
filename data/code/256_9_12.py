def calculate_range(data):
    values = list(data.values())
    if not values:
        return None, None
    min_value = min(values)
    max_value = max(values)
    return min_value, max_value

if __name__ == '__main__':
    sample_data = {
        'label1': 10,
        'label2': 5,
        'label3': 15,
        'label4': 7
    }
    min_val, max_val = calculate_range(sample_data)
    print(f"Range: {min_val} to {max_val}")