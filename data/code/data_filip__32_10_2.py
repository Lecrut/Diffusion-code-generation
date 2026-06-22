def binary_to_hex(binary_str):
    if not binary_str:
        return '0'
    
    if not all(c in '01' for c in binary_str):
        raise ValueError("Input must be a binary string containing only '0' and '1'")
    
    int_value = 0
    for char in binary_str:
        int_value = (int_value << 1) | int(char)
    
    if int_value == 0:
        return '0'
    
    hex_chars = '0123456789ABCDEF'
    hex_digits = []
    
    while int_value > 0:
        hex_digits.append(hex_chars[int_value & 0xF])
        int_value >>= 4
    
    return ''.join(reversed(hex_digits))

if __name__ == '__main__':
    print(binary_to_hex('1111'))
    print(binary_to_hex('00001111'))