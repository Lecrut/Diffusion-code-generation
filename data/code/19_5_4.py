import secrets

def select_secure_random_index(byte_array):
    if not byte_array:
        raise ValueError("Byte array must not be empty")
    length = len(byte_array)
    random_index = secrets.randbelow(length)
    return random_index

if __name__ == '__main__':
    sample_byte_array = b'hello world'
    index = select_secure_random_index(sample_byte_array)
    print(index)