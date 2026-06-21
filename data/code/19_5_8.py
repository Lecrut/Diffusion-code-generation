import secrets
import os

def select_secure_index(byte_array):
    if not byte_array:
        return 0
    index = secrets.randbelow(len(byte_array))
    return index

if __name__ == '__main__':
    sample_bytes = os.urandom(100)
    result_index = select_secure_index(sample_bytes)
    print(result_index)