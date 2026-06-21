def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    if hex_string.startswith(('0x', '0X')):
        hex_string = hex_string[2:]
    if not hex_string:
        return 0
    negative = False
    if hex_string.startswith('-'):
        negative = True
        hex_string = hex_string[1:]
    if not hex_string:
        return 0
    if hex_string.startswith(('0x', '0X')):
        hex_string = hex_string[2:]
    if not hex_string:
        return 0
    result = 0
    for char in hex_string:
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            digit = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            digit = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hex digit: {char}")
        result = result * 16 + digit
    if negative:
        result = -result
    return result

if __name__ == '__main__':
    print(hex_to_decimal("1A3F"))
    print(hex_to_decimal("0x10"))
    print(hex_to_decimal("ff"))
    print(hex_to_decimal("-1A"))
    print(hex_to_decimal("0"))