def binary_to_hex_chunked(binary_string, chunk_size=64):
    if not binary_string:
        return ''
    if not all(c in '01' for c in binary_string):
        raise ValueError('Input must contain only 0 and 1 characters')
    if chunk_size <= 0:
        raise ValueError('Chunk size must be positive')
    
    padded_length = (len(binary_string) + chunk_size - 1) // chunk_size * chunk_size
    padded_binary = binary_string.zfill(padded_length)
    
    hex_map = {}
    for i in range(0, 16):
        hex_map[format(i, '04b')] = format(i, 'x')
    
    result_parts = []
    for i in range(0, len(padded_binary), chunk_size):
        chunk = padded_binary[i:i+chunk_size]
        chunk_len = len(chunk)
        remainder = chunk_len % 4
        if remainder:
            chunk = chunk.zfill(chunk_len + (4 - remainder))
        
        chunk_hex = []
        for j in range(0, len(chunk), 4):
            nibble = chunk[j:j+4]
            chunk_hex.append(hex_map[nibble])
        result_parts.append(''.join(chunk_hex))
    
    return ''.join(result_parts)

if __name__ == '__main__':
    sample_binary_1 = "1101011110011100010111100001"
    sample_binary_2 = "1" * 2000 + "0" * 2000 + "1110"
    
    result1 = binary_to_hex_chunked(sample_binary_1)
    result2 = binary_to_hex_chunked(sample_binary_2)
    
    print(result1)
    print(result2)