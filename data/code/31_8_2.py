COLOR_MAP = {
    "000000": 0,
    "FF0000": 16711680,
    "00FF00": 65280,
    "0000FF": 255,
    "FFFF00": 16776960,
    "00FFFF": 65535,
    "FF00FF": 16711935,
    "FFFFFF": 16777215
}

def hex_to_decimal(hex_color: str) -> int:
    clean_hex = hex_color.lstrip("#").upper()
    if clean_hex in COLOR_MAP:
        return COLOR_MAP[clean_hex]
    try:
        return int(clean_hex, 16)
    except ValueError:
        raise ValueError(f"Invalid hexadecimal color code: {hex_color}")

if __name__ == "__main__":
    sample_codes = ["000000", "FF0000", "123456", "#AABBCC"]
    for code in sample_codes:
        print(hex_to_decimal(code))