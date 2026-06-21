import secrets

def select_secure_random_index(byte_array):
    length = len(byte_array)
    if length == 0:
        raise ValueError("Byte array cannot be empty")
    random_index = secrets.randbelow(length)
    return random_index

if __name__ == '__main__':
    sample_byte_array = bytes([10, 20, 30, 40, 50])
    selected_index = select_secure_random_index(sample_byte_array)
    print(selected_index)