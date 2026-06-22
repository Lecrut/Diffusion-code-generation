def find_min_max_keys(d):
    min_key = max_key = None
    min_val = float('inf')
    max_val = float('-inf')
    
    for key, value in d.items():
        if value < min_val:
            min_val = value
            min_key = key
        if value > max_val:
            max_val = value
            max_key = key
    
    return min_key, max_key

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 2}
    print(find_min_max_keys(sample_dict))