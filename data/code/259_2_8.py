def get_min_max(data_tuple):
    if not data_tuple:
        return None, None
    
    minimum = data_tuple[0]
    maximum = data_tuple[0]
    
    for item in data_tuple[1:]:
        if item < minimum:
            minimum = item
        if item > maximum:
            maximum = item
            
    return minimum, maximum

if __name__ == '__main__':
    sample_data = (15, 3, 88, 42, 9, 77)
    min_val, max_val = get_min_max(sample_data)
    print(f"Data: {sample_data}")
    print(f"Minimum value: {min_val}, Maximum value: {max_val}")