def binary_to_hex(binary_str: str) -> str:
    if not binary_str:
        return ''
    if len(binary_str) % 2 != 0:
        binary_str = '0' * (2 - len(binary_str) % 2) + binary_str
    chunks = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    hex_parts = []
    for chunk in chunks:
        value = int(chunk, 2)
        hex_parts.append(format(value, '0{}x'.format(len(chunk) // 4)))
    return ''.join(hex_parts)

if __name__ == '__main__':
    sample_binary = '101010111100110111100011'
    result = binary_to_hex(sample_binary)
    print(result)
    sample_empty = ''
    result_empty = binary_to_hex(sample_empty)
    print(result_empty)
    sample_odd = '101'
    result_odd = binary_to_hex(sample_odd)
    print(result_odd)