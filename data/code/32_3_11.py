def binary_to_hex(binary_string):
    hex_lookup = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    
    cleaned = binary_string.replace(' ', '').replace('0b', '')
    if not cleaned:
        return '0'
    
    while len(cleaned) % 4 != 0:
        cleaned = '0' + cleaned
        
    hex_digits = []
    for i in range(0, len(cleaned), 4):
        chunk = cleaned[i:i+4]
        hex_digits.append(hex_lookup[chunk])
        
    result = ''.join(hex_digits)
    leading_zeros = True
    final_result = []
    for digit in result:
        if digit == '0' and leading_zeros:
            continue
        else:
            leading_zeros = False
            final_result.append(digit)
            
    if not final_result:
        return '0'
    return ''.join(final_result)

if __name__ == '__main__':
    print(binary_to_hex('11110000'))
    print(binary_to_hex('1010'))
    print(binary_to_hex('00000000'))
    print(binary_to_hex('111111111111'))