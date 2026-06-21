def find_max_value(data):
    if not isinstance(data, dict) or not data:
        raise ValueError("Input must be a non-empty dictionary")
    
    return max(data.values())

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 5, 'c': 2, 'd': 9, 'e': 3}
    sample_dict2 = {'x': -10, 'y': -5, 'z': -1}
    sample_dict3 = {}
    
    try:
        max_value1 = find_max_value(sample_dict1)
        print(f"Max value in {sample_dict1}: {max_value1}")
        
        max_value2 = find_max_value(sample_dict2)
        print(f"Max value in {sample_dict2}: {max_value2}")
        
        find_max_value(sample_dict3)
    except ValueError as e:
        print(f"Error caught: {e}")