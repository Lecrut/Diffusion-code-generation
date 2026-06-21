def hex_to_decimal(hex_str):
    if not isinstance(hex_str, str):
        raise ValueError("Input must be a string")
    if not hex_str:
        raise ValueError("Input string is empty")
    cleaned = hex_str
    if hex_str.startswith("0x") or hex_str.startswith("0X"):
        cleaned = hex_str[2:]
    if not cleaned:
        raise ValueError("No hex digits found")
    valid_chars = set("0123456789abcdefABCDEF")
    if not all(c in valid_chars for c in cleaned):
        raise ValueError("Invalid hex character found")
    return int(cleaned, 16)

if __name__ == '__main__':
    print(hex_to_decimal("1A"))
    print(hex_to_decimal("0xFF"))
    print(hex_to_decimal("0"))
    print(hex_to_decimal("deadBEEF"))
    try:
        hex_to_decimal("GHI")
    except ValueError as e:
        print(str(e))
    try:
        hex_to_decimal("")
    except ValueError as e:
        print(str(e))
    try:
        hex_to_decimal("12 34")
    except ValueError as e:
        print(str(e))