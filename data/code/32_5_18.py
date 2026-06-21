def binary_to_hex_chunked(binary_str, chunk_size=1024 * 1024):
    hex_chars = []
    for i in range(0, len(binary_str), chunk_size):
        chunk = binary_str[i:i + chunk_size]
        padded_chunk = chunk.zfill(len(chunk) + (8 - len(chunk) % 8) % 8)
        hex_chunk = int(padded_chunk, 2).to_bytes((len(padded_chunk) + 7) // 8, byteorder='big').hex()
        actual_hex_len = len(chunk) // 4
        hex_chars.append(hex_chunk[-actual_hex_len:] if actual_hex_len > 0 else hex_chunk)
    return ''.join(hex_chars)

if __name__ == '__main__':
    sample_binary = '1010101111001101'
    result = binary_to_hex_chunked(sample_binary)
    print(result)
    large_binary = '1' * (10 * 1024 * 1024)
    large_result = binary_to_hex_chunked(large_binary)
    print(len(large_result))