def binary_to_hex(binary_string: str) -> str:
    if not binary_string:
        return '0'
    
    try:
        value = int(binary_string, 2)
    except ValueError:
        raise ValueError("Invalid binary string")
    
    if value == 0:
        return '0'
    
    hex_digits = '0123456789ABCDEF'
    result = []
    temp = value
    
    while temp > 0:
        remainder = temp & 0xF
        result.append(hex_digits[remainder])
        temp >>= 4
    
    return ''.join(reversed(result))

if __name__ == '__main__':
    print(binary_to_hex('1010'))
    print(binary_to_hex('00001111'))
    print(binary_to_hex('11111111'))
    print(binary_to_hex('1000000000000000'))
    print(binary_to_hex('11010101101010101010101010101010'))