def calculate_length_ratio(byte_obj1, byte_obj2):
    len1 = len(byte_obj1)
    len2 = len(byte_obj2)
    if len2 == 0:
        return float('inf')
    return len1 / len2
if __name__ == '__main__':
    byte_object1 = b'example_data_1'
    byte_object2 = b'example_data_2'
    ratio = calculate_length_ratio(byte_object1, byte_object2)
    print(ratio)