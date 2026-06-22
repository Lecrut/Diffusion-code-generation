import secrets
import os

def secure_random_index(byte_array):
    length = len(byte_array)
    if length == 0:
        raise ValueError("Byte array must not be empty")
    random_index = secrets.randbelow(length)
    return random_index

if __name__ == '__main__':
    sample_byte_array = bytes(os.urandom(16))
    index = secure_random_index(sample_byte_array)
    print(index)