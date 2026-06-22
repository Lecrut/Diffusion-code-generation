def binary_to_hex(binary_str):
    hex_chars = '0123456789abcdef'
    if not binary_str:
        return '0'
    
    total = 0
    length = len(binary_str)
    for char in binary_str:
        total = total * 2 + int(char)
    
    if total == 0:
        return '0'
    
    hex_digits = []
    while total > 0:
        remainder = total % 16
        hex_digits.append(hex_chars[remainder])
        total = total // 16
    
    return ''.join(reversed(hex_digits))

if __name__ == '__main__':
    result = binary_to_hex('1010')
    print(result)
    result2 = binary_to_hex('11111111')
    print(result2)
    result3 = binary_to_hex('1101011010')
    print(result3)