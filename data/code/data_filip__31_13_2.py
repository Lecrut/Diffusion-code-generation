def hex_to_decimal(hex_str: str) -> int:
    result: int = 0
    multiplier: int = 1
    hex_str_lower: str = hex_str.lower().strip()
    if hex_str_lower.startswith("0x"):
        hex_str_lower = hex_str_lower[2:]
    if not hex_str_lower:
        raise ValueError("Empty hex string")
    for char in reversed(hex_str_lower):
        if char in "0123456789":
            digit: int = ord(char) - ord("0")
        elif char in "abcdef":
            digit: int = ord(char) - ord("a") + 10
        else:
            raise ValueError(f"Invalid hex character: {char}")
        result += digit * multiplier
        multiplier *= 16
    return result

if __name__ == '__main__':
    hex_value: str = "1A3F"
    decimal_value: int = hex_to_decimal(hex_value)
    print(decimal_value)