INITIAL_VALUE = float('inf')

def find_min_max(values):
    if not values:
        return None, None
    
    min_val = max_val = INITIAL_VALUE
    for value in values:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4, 8, 6, 7]
    print(find_min_max(sample_values))