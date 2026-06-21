def compute_data_range(data):
    if not data:
        return None
    min_val = max_val = data[0]
    for value in data[1:]:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return (min_val, max_val)

if __name__ == '__main__':
    sample_data = [3.5, 1, 4.2, 0, -2, 7]
    print(compute_data_range(sample_data))