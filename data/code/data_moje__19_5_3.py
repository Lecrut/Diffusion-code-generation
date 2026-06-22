import secrets

def secure_random_index(data):
    if not data:
        raise ValueError("Data cannot be empty")
    max_index = len(data) - 1
    return secrets.randbelow(max_index + 1)

if __name__ == '__main__':
    sample_bytes = b'cryptographic_safety_check_string_12345'
    index = secure_random_index(sample_bytes)
    print(index)
    print(sample_bytes[index])