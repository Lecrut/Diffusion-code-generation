COLOR_MAP = {
    "000000": 0,
    "FF0000": 16711680,
    "00FF00": 65280,
    "0000FF": 255,
    "FFFF00": 16776960,
    "00FFFF": 65535,
    "FF00FF": 16711935,
    "FFFFFF": 16777215,
    "A52A2A": 10804906,
    "808080": 8421504,
}

def hex_to_decimal(hex_color):
    hex_clean = hex_color.strip().lstrip('#')
    if len(hex_clean) != 6:
        raise ValueError("Invalid hex color format")
    try:
        return int(hex_clean, 16)
    except ValueError:
        raise ValueError("Invalid hex characters")

if __name__ == "__main__":
    sample_colors = ["FF0000", "00FF00", "0000FF", "A52A2A"]
    for color in sample_colors:
        result = hex_to_decimal(color)
        print(f"{color}: {result}")