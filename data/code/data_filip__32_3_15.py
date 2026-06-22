def binary_to_hex(binary_str):
    hex_lookup = {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'A',
        '1011': 'B',
        '1100': 'C',
        '1101': 'D',
        '1110': 'E',
        '1111': 'F'
    }
    
    binary_str = binary_str.strip()
    if len(binary_str) % 4 != 0:
        binary_str = binary_str.zfill((len(binary_str) + 3) // 4 * 4)
    
    hex_chars = []
    for i in range(0, len(binary_str), 4):
        nibble = binary_str[i:i+4]
        hex_chars.append(hex_lookup[nibble])
        
    result = ''.join(hex_chars)
    if result.startswith('0') and len(result) > 1:
        result = result.lstrip('0')
        if not result:
            result = '0'
            
    return result

if __name__ == '__main__':
    sample_binary = '11010111011110101011001111001010'
    hex_result = binary_to_hex(sample_binary)
    print(hex_result)