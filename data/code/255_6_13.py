def find_max_element(data):
    if not data:
        raise ValueError("Data cannot be empty")
    
    max_val = data[0]
    for value in data[1:]:
        if value > max_val:
            max_val = value
    
    return max_val

if __name__ == '__main__':
    sample_data = [3, 5, 1, 2, 4]
    print(find_max_element(sample_data))