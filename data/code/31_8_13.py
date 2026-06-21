def hex_to_decimal_mapping():
    hex_colors = {
        "#FF0000": 16711680,
        "#00FF00": 65280,
        "#0000FF": 255,
        "#FFFF00": 16776960,
        "#FF00FF": 16711935,
        "#00FFFF": 16776960,
        "#FFFFFF": 16777215,
        "#000000": 0,
        "#808080": 8388608,
        "#C0C0C0": 12632256
    }
    return hex_colors

if __name__ == '__main__':
    result = hex_to_decimal_mapping()
    for hex_code, decimal_code in result.items():
        print(f"{hex_code}: {decimal_code}")