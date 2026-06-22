COLOR_MAP = {
    "000000": 0,
    "FFFFFF": 16777215,
    "FF0000": 16711680,
    "00FF00": 65280,
    "0000FF": 255,
    "FFFF00": 16776960,
    "00FFFF": 65535,
    "FF00FF": 16711935,
    "808080": 8421504,
    "C0C0C0": 12632256
}

def hex_to_decimal(hex_code):
    if hex_code in COLOR_MAP:
        return COLOR_MAP[hex_code]
    hex_code = hex_code.lstrip('#')
    if len(hex_code) != 6:
        raise ValueError("Invalid hexadecimal color code length")
    try:
        return int(hex_code, 16)
    except ValueError:
        raise ValueError("Invalid hexadecimal characters in color code")

if __name__ == '__main__':
    test_codes = ["000000", "FF0000", "ABC123", "#FFFFFF", "00FF00"]
    for code in test_codes:
        result = hex_to_decimal(code)
        print(f"{code}: {result}")