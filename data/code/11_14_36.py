def calculate_length_ratio(byte_obj1, byte_obj2):
    if not isinstance(byte_obj1, bytes) or not isinstance(byte_obj2, bytes):
        raise ValueError("Both inputs must be of type bytes")
    
    length1 = len(byte_obj1)
    length2 = len(byte_obj2)
    
    if length2 == 0:
        raise ZeroDivisionError("The second byte object has zero length, division by zero is not allowed.")
    
    return length1 / length2

if __name__ == '__main__':
    sample_byte_obj1 = b'Hello'
    sample_byte_obj2 = b'World!'
    
    try:
        ratio = calculate_length_ratio(sample_byte_obj1, sample_byte_obj2)
        print(ratio)
    except Exception as e:
        print(e)