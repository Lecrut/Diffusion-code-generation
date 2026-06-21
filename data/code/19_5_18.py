import secrets
import sys

def select_secure_index(byte_array):
    length = len(byte_array)
    if length == 0:
        raise ValueError("byte_array must not be empty")
    index = secrets.randbelow(length)
    return index

if __name__ == '__main__':
    sample_bytes = bytes([10, 20, 30, 40, 50])
    result_index = select_secure_index(sample_bytes)
    print(result_index)