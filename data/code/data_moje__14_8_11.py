def access_third_element(data_sequence):
    if data_sequence is None:
        raise TypeError("Input sequence must not be None")
    
    try:
        length = len(data_sequence)
    except TypeError:
        raise TypeError("Input object does not support length")
        
    if length < 3:
        raise ValueError("Sequence must contain at least three elements")
        
    return data_sequence[2]

if __name__ == '__main__':
    test_data = [100, 200, 300, 400, 500]
    retrieved_value = access_third_element(test_data)
    print(retrieved_value)