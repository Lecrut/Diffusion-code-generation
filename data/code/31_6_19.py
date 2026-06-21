def hex_to_decimal(hex_str):
    if not isinstance(hex_str, str):
        raise ValueError("Input must be a string")
    cleaned = hex_str.strip()
    if len(cleaned) == 0:
        raise ValueError("Empty string is not a valid hex string")
    if cleaned.lower().startswith(('0x', '0X')):
        cleaned = cleaned[2:]
    if len(cleaned) == 0:
        raise ValueError("Empty string is not a valid hex string")
    for char in cleaned:
        if char not in '0123456789abcdefABCDEF':
            raise ValueError(f"Invalid character '{char}' in hex string")
    try:
        return int(cleaned, 16)
    except ValueError:
        raise ValueError("Invalid hex string")

if __name__ == '__main__':
    samples = ["0x1A", "FF", "0G", "12 34", ""]
    for s in samples:
        try:
            result = hex_to_decimal(s)
            print(result)
        except ValueError as e:
            print(f"Error: {e}")