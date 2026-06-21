def compute_data_range(data):
    if not data:
        return None
    min_val = max_val = data[0]
    for num in data[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return (min_val, max_val)

if __name__ == '__main__':
    sample_data = [3.5, 2, 7, 1, 4.8]
    print(compute_data_range(sample_data))