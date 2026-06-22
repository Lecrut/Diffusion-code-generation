def find_min_max(data_dict):
    if not data_dict:
        return None, None
    min_key = max_key = None
    for key, value in data_dict.items():
        if min_key is None or value < data_dict[min_key]:
            min_key = key
        if max_key is None or value > data_dict[max_key]:
            max_key = key
    return min_key, max_key

if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 5, 'c': 20, 'd': 8, 'e': 15}
    min_key, max_key = find_min_max(sample_data)
    print(f"Data: {sample_data}")
    print(f"Key with minimum value: {min_key}")
    print(f"Key with maximum value: {max_key}")