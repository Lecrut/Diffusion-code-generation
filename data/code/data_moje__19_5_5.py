import secrets
import os

def get_secure_random_index(byte_array):
    if not byte_array:
        raise ValueError("Byte array must not be empty")
    length = len(byte_array)
    index = secrets.randbelow(length)
    return index

if __name__ == '__main__':
    sample_data = bytes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result_index = get_secure_random_index(sample_data)
    print(result_index)