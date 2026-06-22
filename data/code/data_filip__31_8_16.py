COLOR_MAP = {
    "000000": 0,
    "FF0000": 16711680,
    "00FF00": 65280,
    "0000FF": 255,
    "FFFF00": 16776960,
    "00FFFF": 65535,
    "FF00FF": 16711935,
    "FFFFFF": 16777215,
    "808080": 8421504
}

def hex_to_decimal(hex_code):
    hex_code = hex_code.upper().lstrip("#")
    if hex_code in COLOR_MAP:
        return COLOR_MAP[hex_code]
    try:
        return int(hex_code, 16)
    except ValueError:
        raise ValueError(f"Invalid hexadecimal color code: {hex_code}")

if __name__ == '__main__':
    test_codes = ["FF0000", "00FF00", "0000FF", "#000000", "ABC123"]
    for code in test_codes:
        print(f"{code} -> {hex_to_decimal(code)}")