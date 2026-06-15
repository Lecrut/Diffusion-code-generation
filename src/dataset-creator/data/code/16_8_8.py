def css_to_hex(color_name):
    color_map = {
        "red": "#FF0000",
        "blue": "#0000FF",
        "green": "#008000",
        "yellow": "#FFFF00",
        "black": "#000000",
        "white": "#FFFFFF",
        "gray": "#808080"
    }
    return color_map.get(color_name.lower(), "Color not found")
def hex_to_css(hex_code):
    hex_code = hex_code.upper().strip()
    if len(hex_code) == 6:
        r = hex_code[0:2], hex_code[2:4], hex_code[4:6]
        try:
            r_val = int(r[0], 16)
            g_val = int(r[1], 16)
            b_val = int(r[2], 16)
            return f"rgb({r_val}, {g_val}, {b_val})"
        except ValueError:
            return "Invalid hex format"
    elif len(hex_code) == 3:
        r = hex_code[0] * 2
        g = hex_code[1] * 2
        b = hex_code[2] * 2
        return f"rgb({r}, {g}, {b})"
    else:
        return "Invalid length"
if __name__ == '__main__':
    color_names = ["red", "blue", "green", "yellow", "black", "white"]
    print("--- CSS Color Name to Hex Code Mapping ---")
    for name in color_names:
        hex_code = css_to_hex(name)
        print(f"'{name}': {hex_code}")
    print("\n--- Inverse Mapping Demonstration (Hex to RGB) ---")
    hex_colors = ["#FF0000", "#0000FF", "#008000", "#FFFFFF"]
    for hex_code in hex_colors:
        rgb_value = hex_to_css(hex_code)
        print(f"'{hex_code}': {rgb_value}")