import secrets

def secure_random_index(data):
    if not data:
        raise ValueError("Data cannot be empty")
    return secrets.randbelow(len(data))

if __name__ == '__main__':
    sample_bytes = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a'
    result = secure_random_index(sample_bytes)
    print(result)