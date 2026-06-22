def find_min_max(values):
    if not values:
        raise ValueError("List is empty")
    
    min_val = max_val = values[0]
    
    for value in values[1:]:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [34, 78, 12, 56, 90, 23, 89]
    print(find_min_max(sample_values))