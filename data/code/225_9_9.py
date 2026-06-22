def find_min_max(data_dict):
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
    sample_data = {
        'a': 10,
        'b': 5,
        'c': 20,
        'd': -3,
        'e': 15,
        'f': 8,
        'g': 25,
        'h': -10
    }
    
    min_result, max_result = find_min_max(sample_data)
    print(f"Minimum value: {min_result}")
    print(f"Maximum value: {max_result}")
    
    sample_large_data = {
        'x': 1000,
        'y': -500,
        'z': 999,
        'w': 0,
        'v': 5000,
        'u': -100
    }
    
    min_result_large, max_result_large = find_min_max(sample_large_data)
    print(f"Minimum value (large): {min_result_large}")
    print(f"Maximum value (large): {max_result_large}")