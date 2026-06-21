def binary_to_hex(binary_string):
    if not binary_string:
        return '0'
    
    binary_string = binary_string.lstrip('0')
    if not binary_string:
        return '0'
    
    remainder = len(binary_string) % 4
    if remainder != 0:
        binary_string = '0' * (4 - remainder) + binary_string
    
    hex_digits = '0123456789ABCDEF'
    result = []
    
    for i in range(0, len(binary_string), 4):
        chunk = binary_string[i:i+4]
        value = 0
        for bit in chunk:
            value = (value << 1) | (1 if bit == '1' else 0)
        result.append(hex_digits[value])
    
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "000110101110"
    print(binary_to_hex(sample_input))
    sample_input_2 = "00000000"
    print(binary_to_hex(sample_input_2))
    sample_input_3 = "1111"
    print(binary_to_hex(sample_input_3))