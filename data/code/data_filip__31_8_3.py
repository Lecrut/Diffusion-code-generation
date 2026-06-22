COLOR_MAP_HEX = {
    "FF0000": "RED",
    "00FF00": "GREEN",
    "0000FF": "BLUE",
    "FFFF00": "YELLOW",
    "00FFFF": "CYAN",
    "FF00FF": "MAGENTA",
    "FFFFFF": "WHITE",
    "000000": "BLACK",
    "808080": "GRAY",
    "C0C0C0": "LIGHT_GRAY"
}

COLOR_MAP_DEC = {
    "255,0,0": "RED",
    "0,255,0": "GREEN",
    "0,0,255": "BLUE",
    "255,255,0": "YELLOW",
    "0,255,255": "CYAN",
    "255,0,255": "MAGENTA",
    "255,255,255": "WHITE",
    "0,0,0": "BLACK",
    "128,128,128": "GRAY",
    "192,192,192": "LIGHT_GRAY"
}

def hex_to_decimal(hex_code: str) -> str:
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return f"{r},{g},{b}"

def get_color_name_by_hex(hex_code: str) -> str:
    hex_upper = hex_code.upper()
    if hex_upper in COLOR_MAP_HEX:
        return COLOR_MAP_HEX[hex_upper]
    dec_key = hex_to_decimal(hex_upper)
    if dec_key in COLOR_MAP_DEC:
        return COLOR_MAP_DEC[dec_key]
    return "UNKNOWN"

def get_color_name_by_decimal(decimal_str: str) -> str:
    if decimal_str in COLOR_MAP_DEC:
        return COLOR_MAP_DEC[decimal_str]
    for hex_code, name in COLOR_MAP_HEX.items():
        dec_key = hex_to_decimal(hex_code)
        if dec_key == decimal_str:
            return name
    return "UNKNOWN"

if __name__ == '__main__':
    hex_colors = ["FF0000", "00FF00", "0000FF", "FFFF00", "000000"]
    results = []
    for hc in hex_colors:
        dec = hex_to_decimal(hc)
        name = get_color_name_by_hex(hc)
        results.append(f"Hex: {hc} -> Dec: {dec} -> Name: {name}")
    
    for line in results:
        print(line)
    
    dec_input = "255,0,0"
    name_from_dec = get_color_name_by_decimal(dec_input)
    print(f"Decimal: {dec_input} -> Name: {name_from_dec}")