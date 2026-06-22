def find_min_max(data_tuple):
    if not data_tuple:
        return None, None
    
    min_val = max_val = data_tuple[0]
    
    for item in data_tuple[1:]:
        if item < min_val:
            min_val = item
        elif item > max_val:
            max_val = item
            
    return min_val, max_val

if __name__ == '__main__':
    sample_data = (15, 3, 88, 42, 9, 77)
    min_val, max_val = find_min_max(sample_data)
    print(f"Data: {sample_data}")
    print(f"Minimum value: {min_val}, Maximum value: {max_val}")