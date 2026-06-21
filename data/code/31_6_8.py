def hex_to_decimal(hex_str: str) -> int:
    if not isinstance(hex_str, str):
        raise ValueError("Input must be a string")
    stripped = hex_str.strip()
    if len(stripped) == 0:
        raise ValueError("Input cannot be empty")
    lower = stripped.lower()
    if lower.startswith("0x"):
        valid_chars = set("0123456789abcdef")
        payload = lower[2:]
        if len(payload) == 0:
            raise ValueError("Invalid hex string")
        for char in payload:
            if char not in valid_chars:
                raise ValueError(f"Invalid hex character: {char}")
        return int(stripped, 16)
    else:
        valid_chars = set("0123456789abcdef")
        payload = lower
        if len(payload) == 0:
            raise ValueError("Invalid hex string")
        for char in payload:
            if char not in valid_chars:
                raise ValueError(f"Invalid hex character: {char}")
        return int(stripped, 16)

if __name__ == '__main__':
    samples = ["0xFF", "1A3", "ff", "00", "-10"]
    for s in samples:
        try:
            result = hex_to_decimal(s)
            print(result)
        except ValueError as e:
            print(f"Error: {e}")