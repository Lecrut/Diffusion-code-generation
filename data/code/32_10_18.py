def binary_to_hex(binary_str):
    binary_str = binary_str.lstrip('0') or '0'
    bit_length = len(binary_str)
    if bit_length % 4 != 0:
        binary_str = '0' * (4 - (bit_length % 4)) + binary_str
    
    hex_digits = '0123456789ABCDEF'
    hex_result = []
    
    for i in range(0, len(binary_str), 4):
        nibble = binary_str[i:i+4]
        value = 0
        for bit in nibble:
            value = (value << 1) | (1 if bit == '1' else 0)
        hex_result.append(hex_digits[value])
    
    return ''.join(hex_result)

if __name__ == '__main__':
    sample_values = ['00001111', '10101010', '00000001', '0', '111111111111']
    for val in sample_values:
        print(binary_to_hex(val))