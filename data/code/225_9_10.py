def find_min_max(values):
    if not values:
        return None, None
    
    min_val = max_val = next(iter(values.values()))
    
    for value in values.values():
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
            
    return min_val, max_val

if __name__ == '__main__':
    sample_values = {
        'a': 10,
        'b': 5,
        'c': 20,
        'd': 3
    }
    
    print(find_min_max(sample_values))