def calculate_range(data):
    if not data:
        return None
    min_val = max_val = data[0]
    for value in data[1:]:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return max_val - min_val

if __name__ == '__main__':
    sample_data = [3, 5, 1, 2, 4]
    print(calculate_range(sample_data))