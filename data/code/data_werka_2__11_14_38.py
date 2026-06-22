def calculate_length_ratio(byte_obj1, byte_obj2):
    if not isinstance(byte_obj1, bytes) or not isinstance(byte_obj2, bytes):
        raise ValueError("Both objects must be of type bytes")
    
    length1 = len(byte_obj1)
    length2 = len(byte_obj2)
    
    if length2 == 0:
        raise ZeroDivisionError("The second byte object cannot have zero length")
    
    return length1 / length2

if __name__ == '__main__':
    byte_obj1 = b'example_data_1'
    byte_obj2 = b'example_data_2'
    
    ratio = calculate_length_ratio(byte_obj1, byte_obj2)
    print(ratio)