import secrets
import os

def secure_random_byte_index(byte_array):
    if not byte_array:
        raise ValueError("Byte array cannot be empty")
    length = len(byte_array)
    max_bytes_for_index = (length - 1).bit_length()
    byte_count = (max_bytes_for_index + 7) // 8
    if byte_count == 0:
        return 0
    while True:
        random_bytes = secrets.token_bytes(byte_count)
        random_int = int.from_bytes(random_bytes, 'big')
        if random_int < length:
            return random_int

if __name__ == '__main__':
    sample_data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'
    selected_index = secure_random_byte_index(sample_data)
    print(f"Selected index: {selected_index}")
    print(f"Value at index: {sample_data[selected_index]}")