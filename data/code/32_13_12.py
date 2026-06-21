def binary_to_hex(binary_string):
    hex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    padded_length = len(binary_string) if len(binary_string) % 4 == 0 else len(binary_string) + (4 - len(binary_string) % 4)
    padded_binary = binary_string.zfill(padded_length)
    hex_result = []
    for i in range(0, len(padded_binary), 4):
        chunk = padded_binary[i:i+4]
        hex_result.append(hex_map[chunk])
    return ''.join(hex_result)

if __name__ == '__main__':
    sample_binary = '1101011010'
    result = binary_to_hex(sample_binary)
    print(result)