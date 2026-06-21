def binary_to_hexadecimal(binary_string):
    if not binary_string:
        return ''
    
    valid_chars = set('01')
    if not all(c in valid_chars for c in binary_string):
        raise ValueError("Input must contain only 0s and 1s")
    
    decimal_value = 0
    length = len(binary_string)
    
    for i, char in enumerate(binary_string):
        if char == '1':
            decimal_value |= (1 << (length - 1 - i))
    
    if decimal_value == 0:
        return '0'
    
    hex_digits = []
    while decimal_value > 0:
        remainder = decimal_value & 0xF
        if remainder < 10:
            hex_digits.append(str(remainder))
        else:
            hex_digits.append(chr(ord('A') + remainder - 10))
        decimal_value >>= 4
    
    return ''.join(reversed(hex_digits))

if __name__ == '__main__':
    sample_inputs = ['0000', '0001', '1111', '1010', '10101010', '1111000011110000']
    for s in sample_inputs:
        print(binary_to_hexadecimal(s))