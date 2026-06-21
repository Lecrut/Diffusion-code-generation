import codecs

def binary_string_to_hex(binary_str: str) -> str:
    if not binary_str:
        return ''
    result = []
    chunk_size = 1024 * 1024
    for i in range(0, len(binary_str), chunk_size):
        chunk = binary_str[i:i + chunk_size]
        chunk_bytes = bytes([int(chunk[j:j + 8], 2) for j in range(0, len(chunk), 8)])
        hex_chunk = chunk_bytes.hex()
        result.append(hex_chunk)
    return ''.join(result)
if __name__ == '__main__':
    sample_binary = '00001111' * 100
    hex_output = binary_string_to_hex(sample_binary)
    print(hex_output)