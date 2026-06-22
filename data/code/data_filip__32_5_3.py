def binary_to_hex_chunked(binary_string, chunk_size=1024):
    hex_chars = []
    for i in range(0, len(binary_string), chunk_size):
        chunk = binary_string[i:i + chunk_size]
        num = int(chunk, 2)
        hex_str = format(num, 'x')
        expected_len = (len(chunk) + 3) // 4
        hex_str = hex_str.zfill(expected_len)
        hex_chars.append(hex_str)
    return ''.join(hex_chars)

if __name__ == '__main__':
    sample_binary = '110101101001000101011011'
    result = binary_to_hex_chunked(sample_binary)
    print(result)