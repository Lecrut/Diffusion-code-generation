def binary_to_hex(binary_string):
    if not binary_string:
        return ""
    
    padded_length = (len(binary_string) + 3) // 4 * 4
    binary_string = binary_string.zfill(padded_length)
    
    hex_digits = []
    hex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    
    for i in range(0, len(binary_string), 4):
        chunk = binary_string[i:i+4]
        hex_digits.append(hex_map[chunk])
    
    return ''.join(hex_digits)

if __name__ == '__main__':
    binary_data = "1111000010101010"
    result = binary_to_hex(binary_data)
    print(result)