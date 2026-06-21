def hex_to_decimal_map():
    hardcoded_hex_colors = {
        "red": "FF0000",
        "green": "00FF00",
        "blue": "0000FF",
        "yellow": "FFFF00",
        "cyan": "00FFFF",
        "magenta": "FF00FF",
        "white": "FFFFFF",
        "black": "000000"
    }
    decimal_map = {}
    for name, hex_code in hardcoded_hex_colors.items():
        decimal_value = int(hex_code, 16)
        decimal_map[name] = decimal_value
    return decimal_map

if __name__ == '__main__':
    result = hex_to_decimal_map()
    print(result)