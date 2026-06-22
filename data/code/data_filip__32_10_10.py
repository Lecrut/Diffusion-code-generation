def binary_to_hex(binary_str):
    if not binary_str:
        return '0'
    
    valid_chars = set('01')
    if not all(c in valid_chars for c in binary_str):
        raise ValueError("Input string must contain only '0' and '1'")
    
    if all(c == '0' for c in binary_str):
        return '0'
    
    decimal_value = 0
    for char in binary_str:
        decimal_value = (decimal_value << 1) | int(char)
    
    if decimal_value == 0:
        return '0'
    
    hex_digits = "0123456789ABCDEF"
    hex_result = []
    
    if decimal_value == 0:
        return '0'
        
    while decimal_value > 0:
        remainder = decimal_value & 0xF
        hex_result.append(hex_digits[remainder])
        decimal_value >>= 4
        
    return ''.join(reversed(hex_result))

if __name__ == '__main__':
    print(binary_to_hex('1010'))
    print(binary_to_hex('1111'))
    print(binary_to_hex('0000'))
    print(binary_to_hex('111100001010'))
    print(binary_to_hex('1'))
    print(binary_to_hex('00101'))