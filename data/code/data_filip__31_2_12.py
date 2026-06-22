def hex_to_decimal(hex_str):
    hex_str = hex_str.strip()
    if hex_str.startswith("0x") or hex_str.startswith("0X"):
        hex_str = hex_str[2:]
    if not hex_str:
        return 0
    result = 0
    for char in hex_str:
        result *= 16
        if '0' <= char <= '9':
            result += ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            result += ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            result += ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hexadecimal digit: {char}")
    return result

if __name__ == '__main__':
    print(hex_to_decimal("1A"))
    print(hex_to_decimal("1a"))
    print(hex_to_decimal("FF"))
    print(hex_to_decimal("0x0"))
    print(hex_to_decimal("DEAD"))