def find_min_value(data):
    if not data:
        raise ValueError("Data sequence is empty")
    min_val = float('inf')
    for value in data:
        if value < min_val:
            min_val = value
    return min_val

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_min_value(sample_data))