def find_max_value(data_dict):
    if not data_dict:
        raise ValueError("Input dictionary cannot be empty")
    
    values = data_dict.values()
    return max(values)

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 5, 'c': 2, 'd': 9, 'e': 3}
    sample_dict2 = {'x': -10, 'y': -5, 'z': -1}
    sample_dict3 = {}
    
    try:
        result1 = find_max_value(sample_dict1)
        print(f"Max value in {sample_dict1}: {result1}")
        
        result2 = find_max_value(sample_dict2)
        print(f"Max value in {sample_dict2}: {result2}")
        
        find_max_value(sample_dict3)
    except ValueError as e:
        print(f"Error caught: {e}")