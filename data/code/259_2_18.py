def find_min_max(data_tuple):
    if not data_tuple:
        return None, None
    
    min_val = max_val = data_tuple[0]
    
    for item in data_tuple:
        if item < min_val:
            min_val = item
        elif item > max_val:
            max_val = item
    
    return min_val, max_val

if __name__ == '__main__':
    sample_data1 = (10, 5, 20, 8, 15)
    min1, max1 = find_min_max(sample_data1)
    print(f"Data: {sample_data1}")
    print(f"Minimum: {min1}, Maximum: {max1}")

    sample_data2 = (-5, 100, 0, -50)
    min2, max2 = find_min_max(sample_data2)
    print(f"Data: {sample_data2}")
    print(f"Minimum: {min2}, Maximum: {max2}")