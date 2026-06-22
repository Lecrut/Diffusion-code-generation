import secrets

def select_random_index(byte_array: bytes) -> int:
    if len(byte_array) == 0:
        raise ValueError("Byte array must not be empty")
    return secrets.randbelow(len(byte_array))

if __name__ == '__main__':
    sample_bytes = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a'
    random_index = select_random_index(sample_bytes)
    print(random_index)