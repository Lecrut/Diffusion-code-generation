def hex_to_decimal(hex_str):
    if not isinstance(hex_str, str):
        raise TypeError("Input must be a string")
    if hex_str.startswith(('0x', '0X')):
        hex_digits = hex_str[2:]
    else:
        hex_digits = hex_str
    if not hex_digits:
        return 0
    try:
        return int(hex_digits, 16)
    except ValueError:
        raise ValueError(f"Invalid hexadecimal string: {hex_str}")

if __name__ == '__main__':
    print(hex_to_decimal("0x1A"))
    print(hex_to_decimal("0xFF"))
    print(hex_to_decimal("0X10"))
    print(hex_to_decimal("0"))
    print(hex_to_decimal("0x0"))