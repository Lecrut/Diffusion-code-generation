def find_min_value(data):
    if not data:
        raise ValueError("Data sequence is empty")
    
    min_val = data[0]
    for value in data[1:]:
        if value < min_val:
            min_val = value
    
    return min_val

if __name__ == '__main__':
    sample_data = [8, 3, 7, 2, 5]
    print(find_min_value(sample_data))