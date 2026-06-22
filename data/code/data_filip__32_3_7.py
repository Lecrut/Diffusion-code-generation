def binary_to_hex(binary_string):
    hex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    
    padded_bin = binary_string.zfill(len(binary_string) + (4 - len(binary_string) % 4) % 4)
    
    hex_result = []
    for i in range(0, len(padded_bin), 4):
        chunk = padded_bin[i:i+4]
        hex_result.append(hex_map[chunk])
    
    return '0x' + ''.join(hex_result)

if __name__ == '__main__':
    result = binary_to_hex('1101111')
    print(result)