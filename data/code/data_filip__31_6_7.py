def hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    stripped = hex_string.strip()
    if not stripped:
        raise ValueError("Hex string cannot be empty")
    allowed_chars = set("0123456789abcdefABCDEF")
    if not all(c in allowed_chars for c in stripped):
        raise ValueError("Invalid hex character found")
    try:
        return int(stripped, 16)
    except Exception:
        raise ValueError("Failed to convert hex string to decimal")

if __name__ == '__main__':
    print(hex_to_decimal("FF"))
    print(hex_to_decimal("1a3"))
    print(hex_to_decimal("0"))
    print(hex_to_decimal("deadBEEF"))
    try:
        hex_to_decimal("GHI")
    except ValueError as e:
        print("Error:", e)
    try:
        hex_to_decimal("")
    except ValueError as e:
        print("Error:", e)
    try:
        hex_to_decimal(" 12 ")
    except ValueError as e:
        print("Error:", e)