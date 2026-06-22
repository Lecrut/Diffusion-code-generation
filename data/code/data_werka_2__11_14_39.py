def calculate_length_ratio(byte_obj1, byte_obj2):
    length1 = len(byte_obj1)
    length2 = len(byte_obj2)
    if length2 == 0:
        raise ValueError("The second byte object has zero length.")
    return length1 / length2

if __name__ == '__main__':
    byte_obj1 = b'Hello, World!'
    byte_obj2 = b'Python'
    ratio = calculate_length_ratio(byte_obj1, byte_obj2)
    print(ratio)