import sys
import binascii

def binary_to_hex_chunked(binary_string: str) -> str:
    if not binary_string:
        return ""
    
    if len(binary_string) % 4 != 0:
        padded_binary = binary_string.zfill(len(binary_string) + (4 - len(binary_string) % 4))
    else:
        padded_binary = binary_string
    
    hex_parts = []
    chunk_size = 4096
    
    for i in range(0, len(padded_binary), chunk_size):
        chunk = padded_binary[i : i + chunk_size]
        padded_chunk = chunk.zfill(len(chunk) + (4 - len(chunk) % 4) if len(chunk) % 4 else 0)
        binary_bytes = int(padded_chunk, 2).to_bytes((len(padded_chunk) + 7) // 8, byteorder='big')
        hex_parts.append(binascii.hexlify(binary_bytes).decode('ascii'))
    
    return ''.join(hex_parts)

if __name__ == '__main__':
    sample_binary = "1101001110101100111001010101010111110000111100001010101010101010"
    result = binary_to_hex_chunked(sample_binary)
    print(result)