import secrets

def get_secure_random_index(byte_array):
    length = len(byte_array)
    if length == 0:
        raise ValueError("Byte array must not be empty")
    random_index = secrets.randbelow(length)
    return random_index

if __name__ == '__main__':
    sample_byte_array = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a'
    index = get_secure_random_index(sample_byte_array)
    print(index)