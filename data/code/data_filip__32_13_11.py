def binary_to_hex(binary_string):
    clean_binary = binary_string.replace(' ', '')
    if len(clean_binary) == 0:
        return ''
    
    padding_needed = (4 - len(clean_binary) % 4) % 4
    padded_binary = '0' * padding_needed + clean_binary
    
    hex_string = ''
    hex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    
    for i in range(0, len(padded_binary), 4):
        nibble = padded_binary[i:i+4]
        hex_string += hex_map[nibble]
        
    return hex_string

if __name__ == '__main__':
    sample_data = '1111001010011100100100100001'
    result = binary_to_hex(sample_data)
    print(result)