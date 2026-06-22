import secrets

def secure_random_index(byte_array: bytes) -> int:
    if not byte_array:
        raise ValueError("Byte array must not be empty")
    length = len(byte_array)
    random_value = secrets.randbelow(length)
    return random_value

if __name__ == '__main__':
    sample_data = b"cryptographic_security_test"
    result_index = secure_random_index(sample_data)
    print(result_index)
    print(sample_data[result_index])