def calculate_length_ratio(byte_obj1, byte_obj2):
    len1 = len(byte_obj1)
    len2 = len(byte_obj2)
    if len2 == 0:
        raise ValueError("The second byte object cannot have zero length.")
    return len1 / len2

if __name__ == '__main__':
    byte_obj1 = b'Hello, World!'
    byte_obj2 = b'Python'
    ratio = calculate_length_ratio(byte_obj1, byte_obj2)
    print(ratio)