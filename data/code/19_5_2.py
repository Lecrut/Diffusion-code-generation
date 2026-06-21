import secrets

def select_random_byte_index(byte_array):
    index = secrets.randbelow(len(byte_array))
    return index

if __name__ == '__main__':
    sample_bytes = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'
    result = select_random_byte_index(sample_bytes)
    print(result)