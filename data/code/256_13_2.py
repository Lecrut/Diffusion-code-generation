def calculate_range(data):
    min_val = float('inf')
    max_val = float('-inf')
    for value in data:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return max_val - min_val

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(calculate_range(sample_data))