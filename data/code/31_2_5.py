def hex_to_dec(hex_code):
    hex_code = hex_code.strip()
    if hex_code.startswith("0x") or hex_code.startswith("0X"):
        hex_code = hex_code[2:]
    decimal_value = 0
    for char in hex_code:
        decimal_value *= 16
        if '0' <= char <= '9':
            decimal_value += ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            decimal_value += ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            decimal_value += ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hexadecimal digit: {char}")
    return decimal_value

if __name__ == '__main__':
    print(hex_to_dec("FF"))
    print(hex_to_dec("ff"))
    print(hex_to_dec("0x1A3"))
    print(hex_to_dec("0X1A3"))
    print(hex_to_dec("0"))
    print(hex_to_dec("10"))
    print(hex_to_dec("ABCDEF"))
    print(hex_to_dec("abcdef"))