def calculate_length_ratio(byte_obj1, byte_obj2):
    length1 = len(byte_obj1)
    length2 = len(byte_obj2)
    if length2 == 0:
        return float('inf')
    return length1 / length2
if __name__ == '__main__':
    sample_byte_obj1 = b'Hello, World!'
    sample_byte_obj2 = b'Python'
    ratio = calculate_length_ratio(sample_byte_obj1, sample_byte_obj2)
    print(ratio)