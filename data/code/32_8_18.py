def binary_to_hex(binary_string):
    hex_map = '0123456789ABCDEF'
    if not binary_string:
        return '0'
    cleaned = binary_string.lstrip('0')
    if not cleaned:
        return '0'
    while len(cleaned) % 4 != 0:
        cleaned = '0' + cleaned
    result = []
    for i in range(0, len(cleaned), 4):
        nibble = cleaned[i:i+4]
        val = int(nibble, 2)
        result.append(hex_map[val])
    return ''.join(result)

if __name__ == '__main__':
    samples = ['1010', '11110000', '0000', '1', '0001010', '110011001100', '']
    for s in samples:
        print(binary_to_hex(s))