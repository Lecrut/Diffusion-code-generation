def binary_to_hex(binary_string: str) -> str:
    if not binary_string:
        return '0'
    
    binary_string = binary_string.lstrip('0')
    
    if not binary_string:
        return '0'
    
    value = 0
    for char in binary_string:
        value = (value << 1) | (1 if char == '1' else 0)
    
    hex_digits = '0123456789ABCDEF'
    hex_result = ''
    
    if value == 0:
        return '0'
    
    while value > 0:
        remainder = value & 15
        hex_result = hex_digits[remainder] + hex_result
        value >>= 4
    
    return hex_result

if __name__ == '__main__':
    test_cases = ['0', '1', '1010', '1111', '10000', '0001010', '11111111']
    for binary in test_cases:
        print(f"{binary} -> {binary_to_hex(binary)}")