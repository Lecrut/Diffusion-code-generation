def binary_to_hex(binary_string: str) -> str:
    if not binary_string:
        return "0"
    try:
        decimal_value = int(binary_string, 2)
    except ValueError:
        raise ValueError("Invalid binary string")
    
    if decimal_value == 0:
        return "0"
    
    hex_chars = "0123456789ABCDEF"
    hex_digits = []
    
    while decimal_value > 0:
        remainder = decimal_value % 16
        hex_digits.append(hex_chars[remainder])
        decimal_value //= 16
    
    hex_digits.reverse()
    return ''.join(hex_digits)

if __name__ == '__main__':
    print(binary_to_hex("1010"))
    print(binary_to_hex("0000"))
    print(binary_to_hex("11111111"))
    print(binary_to_hex("101010101010"))