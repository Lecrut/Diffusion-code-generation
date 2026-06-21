def compute_data_range(data):
    min_val = float('inf')
    max_val = float('-inf')
    for value in data:
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value
    return (min_val, max_val)

if __name__ == '__main__':
    sample_data = [3.14, 2.718, 100, -50, 0]
    print(compute_data_range(sample_data))