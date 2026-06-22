def calculate_value_difference(data):
    if not data:
        return 0
    max_val = max(data.values())
    min_val = min(data.values())
    return max_val - min_val

if __name__ == '__main__':
    sample_data = {
        'x': 15,
        'y': 25,
        'z': 5,
        'w': 35
    }
    result = calculate_value_difference(sample_data)
    print(result)