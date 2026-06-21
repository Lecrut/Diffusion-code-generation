def hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    cleaned = hex_string
    if cleaned.startswith('0x') or cleaned.startswith('0X'):
        cleaned = cleaned[2:]
    if len(cleaned) == 0:
        raise ValueError("Empty hex string")
    allowed = set("0123456789abcdefABCDEF")
    for char in cleaned:
        if char not in allowed:
            raise ValueError("Invalid hex character: {}".format(char))
    return int(cleaned, 16)

if __name__ == '__main__':
    print(hex_to_decimal("FF"))
    print(hex_to_decimal("0x1A"))
    print(hex_to_decimal("deadBEEF"))
    print(hex_to_decimal("0"))
    print(hex_to_decimal("123456789abcdef"))
    try:
        hex_to_decimal("GHI")
    except ValueError as e:
        print(e)
    try:
        hex_to_decimal("")
    except ValueError as e:
        print(e)
    try:
        hex_to_decimal("12 34")
    except ValueError as e:
        print(e)