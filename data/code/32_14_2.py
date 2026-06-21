def binary_to_hex(binary_string):
    if not binary_string:
        return ''
    if len(binary_string) % 4 != 0:
        binary_string = binary_string.zfill((len(binary_string) + 3) // 4 * 4)
    byte_list = bytearray()
    for i in range(0, len(binary_string), 8):
        byte_str = binary_string[i:i+8]
        if len(byte_str) < 8:
            byte_str = byte_str.zfill(8)
        byte_list.append(int(byte_str, 2))
    return byte_list.hex()

if __name__ == '__main__':
    samples = [
        '00000001',
        '11111111',
        '00000000',
        '10101010',
        '00000010',
        '111100001111000011110000',
        '',
        '1',
        '10',
        '100',
        '1000',
        '10000',
    ]
    for sample in samples:
        result = binary_to_hex(sample)
        print(result)