def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    if hex_string.startswith("0x") or hex_string.startswith("0X"):
        hex_string = hex_string[2:]
    negative = hex_string.startswith("-")
    if negative:
        hex_string = hex_string[1:]
    result = 0
    power = 0
    for char in reversed(hex_string):
        char = char.lower()
        if '0' <= char <= '9':
            value = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            value = ord(char) - ord('a') + 10
        else:
            raise ValueError("Invalid hexadecimal digit")
        result += value * (16 ** power)
        power += 1
    if negative:
        result = -result
    return result

if __name__ == '__main__':
    print(hex_to_decimal("1A"))
    print(hex_to_decimal("0xFF"))
    print(hex_to_decimal("-2B"))
    print(hex_to_decimal("0"))
    print(hex_to_decimal("10"))