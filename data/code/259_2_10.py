def find_min_max(data_tuple):
    if not data_tuple:
        return None, None

    MIN = float('inf')
    MAX = float('-inf')

    for item in data_tuple:
        if item < MIN:
            MIN = item
        if item > MAX:
            MAX = item

    return MIN, MAX

if __name__ == '__main__':
    sample_data = (15, 3, 88, 42, 9, 77)
    min_val, max_val = find_min_max(sample_data)
    print(f"Data: {sample_data}")
    print(f"Minimum value: {min_val}, Maximum value: {max_val}")