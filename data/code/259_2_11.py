def find_min_max(data_tuple):
    if not data_tuple:
        return None, None
    
    min_val = data_tuple[0]
    max_val = data_tuple[0]
    
    for value in data_tuple:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    
    return min_val, max_val

if __name__ == '__main__':
    sample_data = (34, 12, 78, 90, 56, 23)
    min_val, max_val = find_min_max(sample_data)
    print(f"Data: {sample_data}, Minimum: {min_val}, Maximum: {max_val}")