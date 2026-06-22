def compute_value_range(data):
    if not data:
        return 0
    max_value = float('-inf')
    min_value = float('inf')
    for value in data.values():
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
    return max_value - min_value

if __name__ == '__main__':
    sample_data = {
        'x': 7,
        'y': 15,
        'z': 3,
        'w': 22
    }
    print(compute_value_range(sample_data))