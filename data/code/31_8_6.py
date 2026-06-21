def hex_to_decimal():
    hex_colors = {
        "FF0000": "red",
        "00FF00": "green",
        "0000FF": "blue",
        "FFFF00": "yellow",
        "00FFFF": "cyan",
        "FF00FF": "magenta",
        "FFFFFF": "white",
        "000000": "black",
        "C0C0C0": "silver",
        "808080": "gray"
    }
    decimal_map = {}
    for hex_code, name in hex_colors.items():
        decimal_value = int(hex_code, 16)
        decimal_map[name] = decimal_value
    return decimal_map

if __name__ == "__main__":
    result = hex_to_decimal()
    print(result)