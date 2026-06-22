import secrets

def secure_random_index(byte_array):
    if not byte_array:
        raise ValueError("Byte array must not be empty")
    length = len(byte_array)
    return secrets.randbelow(length)

if __name__ == '__main__':
    sample_data = bytes([0x48, 0x65, 0x6C, 0x6C, 0x6F, 0x21])
    selected_index = secure_random_index(sample_data)
    print(selected_index)
    print(sample_data[selected_index])