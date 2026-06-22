def hex_to_decimal(hex_str):
    if not isinstance(hex_str, str) or len(hex_str) == 0:
        raise ValueError("Invalid hex string")
    hex_chars = "0123456789ABCDEFabcdef"
    result = 0
    is_negative = False
    start_index = 0
    if hex_str[0] == '-':
        is_negative = True
        start_index = 1
    if len(hex_str) == start_index:
        raise ValueError("Invalid hex string")
    if hex_str[start_index] == '0' and len(hex_str) > start_index + 1 and (hex_str[start_index + 1] == 'x' or hex_str[start_index + 1] == 'X'):
        start_index += 2
    if start_index >= len(hex_str):
        raise ValueError("Invalid hex string")
    for char in hex_str[start_index:]:
        if char not in hex_chars:
            raise ValueError(f"Invalid character in hex string: {char}")
        if '0' <= char <= '9':
            val = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            val = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            val = ord(char) - ord('A') + 10
        else:
            val = 0
        result = result * 16 + val
    if is_negative:
        result = -result
    return result

if __name__ == '__main__':
    print(hex_to_decimal("FF"))
    print(hex_to_decimal("ff"))
    print(hex_to_decimal("10"))
    print(hex_to_decimal("0x1A"))
    print(hex_to_decimal("-FF"))
    print(hex_to_decimal("ABCDEF"))
    print(hex_to_decimal("0"))
    print(hex_to_decimal("0x0"))