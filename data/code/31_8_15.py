COLOR_MAP = {
    "FF0000": 16711680,
    "00FF00": 65280,
    "0000FF": 255,
    "FFFFFF": 16777215,
    "000000": 0
}

def hex_to_decimal(hex_code: str) -> int:
    if hex_code in COLOR_MAP:
        return COLOR_MAP[hex_code]
    return int(hex_code, 16)

if __name__ == "__main__":
    sample_codes = ["FF0000", "00FF00", "ABCDEF"]
    for code in sample_codes:
        print(hex_to_decimal(code))