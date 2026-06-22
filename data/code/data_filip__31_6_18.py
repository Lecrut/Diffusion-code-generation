def hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    if not hex_string:
        raise ValueError("Input string is empty")
    allowed = set("0123456789abcdefABCDEF")
    for char in hex_string:
        if char not in allowed:
            raise ValueError(f"Invalid character in hex string: {char}")
    return int(hex_string, 16)

if __name__ == '__main__':
    print(hex_to_decimal("1A"))
    print(hex_to_decimal("FF"))
    print(hex_to_decimal("0"))
    try:
        print(hex_to_decimal("G1"))
    except ValueError as e:
        print(e)
    try:
        print(hex_to_decimal(""))
    except ValueError as e:
        print(e)
    try:
        print(hex_to_decimal("12 3"))
    except ValueError as e:
        print(e)