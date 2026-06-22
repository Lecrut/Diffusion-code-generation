def calculate_length_ratio(byte_obj1, byte_obj2):
    length1 = len(byte_obj1)
    length2 = len(byte_obj2)
    if length2 == 0:
        return float('inf') if length1 > 0 else 0.0
    return length1 / length2

if __name__ == '__main__':
    byte_object1 = b'example_data_1'
    byte_object2 = b'example_data_2_with_more_length'
    ratio = calculate_length_ratio(byte_object1, byte_object2)
    print(ratio)