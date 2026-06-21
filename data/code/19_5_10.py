import secrets
import random

def secure_random_index(byte_array: bytes) -> int:
    length = len(byte_array)
    if length == 0:
        raise ValueError("Byte array must not be empty")
    if length == 1:
        return 0
    secure_random = secrets.SystemRandom()
    return secure_random.randrange(length)

if __name__ == '__main__':
    sample_data = bytes([0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09])
    index = secure_random_index(sample_data)
    print(index)