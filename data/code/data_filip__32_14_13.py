def binary_to_hex(binary_str):
    if not binary_str:
        return ''
    normalized = binary_str.lstrip('0') or '0'
    padded_length = len(normalized)
    padding_needed = (8 - (padded_length % 8)) % 8
    padded = '0' * padding_needed + normalized
    byte_length = len(padded) // 8
    byte_array = bytearray(byte_length)
    for i in range(byte_length):
        chunk = padded[i * 8:(i + 1) * 8]
        byte_array[i] = int(chunk, 2)
    hex_result = byte_array.hex()
    if padding_needed > 0:
        leading_zeros = padding_needed // 4
        if padding_needed % 4 != 0:
            leading_zeros += 1
        hex_result = hex_result[leading_zeros:] or '0'
    return hex_result

if __name__ == '__main__':
    sample_binaries = [
        '1010',
        '11110000',
        '00000000',
        '1111111111111111',
        '1000000000000001',
        '',
        '0',
        '1',
        '110100101011'
    ]
    for b in sample_binaries:
        result = binary_to_hex(b)
        print(f"binary_to_hex('{b}') = '{result}'")