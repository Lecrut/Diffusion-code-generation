import os
import struct

def binary_to_hex_chunked(binary_data, chunk_size=1048576):
    if not isinstance(binary_data, bytes):
        raise TypeError("Input must be bytes")

    hex_parts = []
    for i in range(0, len(binary_data), chunk_size):
        chunk = binary_data[i:i + chunk_size]
        hex_parts.append(chunk.hex())

    return ''.join(hex_parts)

def hex_to_binary_chunked(hex_string, chunk_size=2097152):
    if not isinstance(hex_string, str):
        raise TypeError("Input must be a string")

    if len(hex_string) % 2 != 0:
        raise ValueError("Hex string must have even length")

    binary_parts = bytearray()
    for i in range(0, len(hex_string), chunk_size):
        chunk_hex = hex_string[i:i + chunk_size]
        if len(chunk_hex) % 2 != 0:
            chunk_hex += '0'
        chunk_bytes = bytes.fromhex(chunk_hex)
        binary_parts.extend(chunk_bytes)

    return bytes(binary_parts)

if __name__ == '__main__':
    sample_binary = os.urandom(1048576)
    hex_result = binary_to_hex_chunked(sample_binary)
    print(len(hex_result))
    reconstructed = hex_to_binary_chunked(hex_result)
    print(sample_binary == reconstructed)