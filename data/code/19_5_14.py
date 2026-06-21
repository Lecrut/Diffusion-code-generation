import secrets

def get_secure_index(byte_array):
    if not byte_array:
        return 0
    return secrets.randbelow(len(byte_array))

if __name__ == '__main__':
    sample_bytes = b'0123456789ABCDEF'
    index = get_secure_index(sample_bytes)
    print(index)