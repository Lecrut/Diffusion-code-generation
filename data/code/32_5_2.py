def binary_to_hex_chunked(binary_string, chunk_size=8192):
    hex_chunks = []
    for i in range(0, len(binary_string), chunk_size):
        chunk = binary_string[i:i + chunk_size]
        hex_chunks.append(int(chunk, 2).hex())
    return ''.join(hex_chunks)

if __name__ == '__main__':
    sample_binary = '1111111100000000111100001111000011110000111100001111000011110000'
    result = binary_to_hex_chunked(sample_binary)
    print(result)