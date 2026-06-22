def find_min_max(dictionary):
    if not dictionary:
        raise ValueError("Dictionary is empty")
    
    min_val = max_val = next(iter(dictionary.values()))
    
    for value in dictionary.values():
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    
    return min_val, max_val

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 30}
    try:
        min_value, max_value = find_min_max(sample_dict)
        print(f"Minimum value: {min_value}, Maximum value: {max_value}")
    except ValueError as e:
        print(e)