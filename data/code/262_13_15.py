def find_min_max(data_dict):
    if not data_dict:
        return None, None
    min_key = max_key = None
    min_val = float('inf')
    max_val = float('-inf')
    for key, value in data_dict.items():
        if value < min_val:
            min_val = value
            min_key = key
        if value > max_val:
            max_val = value
            max_key = key
    return min_key, max_key

if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 5, 'c': 20, 'd': 8, 'e': 15}
    min_key, max_key = find_min_max(sample_data)
    print(f"Data: {sample_data}")
    print(f"Key with minimum value: {min_key}, Value: {sample_data[min_key]}")
    print(f"Key with maximum value: {max_key}, Value: {sample_data[max_key]}")