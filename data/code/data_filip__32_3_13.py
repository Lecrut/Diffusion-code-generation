def binary_to_hex(binary_str):
    lookup = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    padded = binary_str.zfill((len(binary_str) + 3) // 4 * 4)
    result = []
    for i in range(0, len(padded), 4):
        nibble = padded[i:i + 4]
        result.append(lookup[nibble])
    hex_result = ''.join(result)
    hex_result = hex_result.lstrip('0')
    return hex_result if hex_result else '0'

if __name__ == '__main__':
    print(binary_to_hex('1010'))
    print(binary_to_hex('11111111'))
    print(binary_to_hex('0'))