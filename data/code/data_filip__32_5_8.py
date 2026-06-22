import struct
import binascii

def binary_to_hex_chunked(binary_data, chunk_size=1024 * 1024):
    if isinstance(binary_data, str):
        binary_data = binary_data.encode('ascii')
    hex_chunks = []
    for i in range(0, len(binary_data), chunk_size):
        chunk = binary_data[i:i + chunk_size]
        hex_chunks.append(binascii.hexlify(chunk).decode('ascii'))
    return ''.join(hex_chunks)

if __name__ == '__main__':
    sample_binary = bytes(range(256)) * 1000
    result = binary_to_hex_chunked(sample_binary)
    print(result[:64])
    print(len(result))