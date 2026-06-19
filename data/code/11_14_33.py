def calculate_length_ratio(byte_obj1, byte_obj2):
    len1 = len(byte_obj1)
    len2 = len(byte_obj2)
    if len2 == 0:
        return float('inf')
    return len1 / len2

if __name__ == '__main__':
    sample_byte_obj1 = b'hello'
    sample_byte_obj2 = b'world'
    ratio = calculate_length_ratio(sample_byte_obj1, sample_byte_obj2)
    print(ratio)