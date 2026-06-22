def find_min_max_dict(data_dict):
    if not data_dict:
        return None, None
    min_val = float('inf')
    max_val = float('-inf')
    for value in data_dict.values():
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value
    return min_val, max_val

if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 5, 'c': 20, 'd': -3, 'e': 15, 'f': 8, 'g': 25, 'h': -10}
    min_result, max_result = find_min_max_dict(sample_data)
    print(f"Minimum value: {min_result}")
    print(f"Maximum value: {max_result}")