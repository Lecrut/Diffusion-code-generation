def hex_to_decimal(hex_str):
    hex_str = hex_str.strip()
    if hex_str.lower().startswith('0x'):
        hex_str = hex_str[2:]
    result = 0
    for char in hex_str:
        digit = 0
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            digit = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            digit = ord(char) - ord('A') + 10
        else:
            raise ValueError("Invalid hexadecimal digit: {}".format(char))
        result = result * 16 + digit
    return result

if __name__ == '__main__':
    print(hex_to_decimal("1A"))
    print(hex_to_decimal("ff"))
    print(hex_to_decimal("0X2F"))
    print(hex_to_decimal("ABCDEF"))
    print(hex_to_decimal("0"))
    print(hex_to_decimal("10"))