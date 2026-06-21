def hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    cleaned = hex_string.strip()
    if cleaned.lower().startswith('0x'):
        cleaned = cleaned[2:]
    if not cleaned:
        raise ValueError("Empty hex string")
    for char in cleaned:
        if char.lower() not in '0123456789abcdef':
            raise ValueError("Invalid hex character: {}".format(char))
    return int(cleaned, 16)

if __name__ == '__main__':
    print(hex_to_decimal("1A"))
    print(hex_to_decimal("0xFF"))
    print(hex_to_decimal("deadBEEF"))
    try:
        hex_to_decimal("GHIJ")
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