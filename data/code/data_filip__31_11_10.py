def hex_to_decimal(hex_str):
    if not isinstance(hex_str, str):
        return 0
    stripped = hex_str.strip()
    if not stripped:
        return 0
    lower = stripped.lower()
    if lower.startswith('0x'):
        numeric_part = lower[2:]
    else:
        numeric_part = lower
    if not numeric_part:
        return 0
    for char in numeric_part:
        if char not in '0123456789abcdef':
            return 0
    return int(numeric_part, 16)

if __name__ == '__main__':
    print(hex_to_decimal("0x10"))
    print(hex_to_decimal("0XFF"))
    print(hex_to_decimal("0"))
    print(hex_to_decimal("0xGHI"))
    print(hex_to_decimal(""))
    print(hex_to_decimal(None))
    print(hex_to_decimal("0x0"))