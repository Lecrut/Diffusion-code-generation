def get_value_from_list(data, index):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    
    length = len(data)
    
    if index < 0:
        adjusted_index = length + index
        if adjusted_index < 0:
            raise ValueError(f"Index {index} is out of bounds for list of length {length}")
        index = adjusted_index
    
    if index >= length:
        raise ValueError(f"Index {index} is out of bounds for list of length {length}")
    
    return data[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    
    try:
        result = get_value_from_list(sample_list, 2)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        result = get_value_from_list(sample_list, 10)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        result = get_value_from_list(sample_list, -1)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")