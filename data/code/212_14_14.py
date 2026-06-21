def find_min_max(values):
    if not values:
        return None, None
    
    min_val = max_val = values[0]
    
    for value in values[1:]:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
            
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [34, 78, 23, 56, 12, 90, 45]
    print(find_min_max(sample_values))