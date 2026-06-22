HEX_MAP = {
    "FF": 255,
    "7F": 127,
    "00": 0,
    "A0": 160,
    "C0": 192,
}

def map_hex_to_decimal(hex_str: str) -> int:
    normalized = hex_str.upper()
    if normalized in HEX_MAP:
        return HEX_MAP[normalized]
    if len(normalized) == 6 and all(c in "0123456789ABCDEF" for c in normalized):
        return int(normalized, 16)
    if len(normalized) == 2 and all(c in "0123456789ABCDEF" for c in normalized):
        return int(normalized, 16)
    raise ValueError(f"Invalid hexadecimal string: {hex_str}")

def map_color_pair(red_hex: str, green_hex: str, blue_hex: str) -> tuple:
    return (
        map_hex_to_decimal(red_hex),
        map_hex_to_decimal(green_hex),
        map_hex_to_decimal(blue_hex),
    )

if __name__ == "__main__":
    result = map_color_pair("FF", "7F", "00")
    print(result)