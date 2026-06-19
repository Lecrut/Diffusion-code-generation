def calculate_length_ratio(byte_obj1, byte_obj2):
    return len(byte_obj1) / len(byte_obj2)

if __name__ == '__main__':
    byte_obj1 = b'example_data_1'
    byte_obj2 = b'short_data'
    ratio = calculate_length_ratio(byte_obj1, byte_obj2)
    print(ratio)