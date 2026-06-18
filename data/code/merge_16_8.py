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
            r_int = tuple(int(x, 16) for x in r)
            return f"rgb({r_int[0]}, {r_int[1]}, {r_int[2]})"
        except ValueError:
            return "Invalid hex format"
    elif len(hex_code) == 3:
        r = hex_code[0]
        g = hex_code[1]
        b = hex_code[2]
        try:
            r_int = int(r, 16)
            g_int = int(g, 16)
            b_int = int(b, 16)
            return f"rgb({r_int}, {g_int}, {b_int})"
        except ValueError:
            return "Invalid RGB format"
    return "Invalid hex code length"
if __name__ == '__main__':
    color_names = ["red", "blue", "green", "yellow", "black", "white"]
    print("--- CSS Color Name to Hex Code Mapping ---")
    for name in color_names:
        hex_code = css_to_hex(name)
        print(f"'{name}': {hex_code}")
    print("\n--- Inverse Mapping Demonstration (Hex to RGB) ---")
    hex_samples = ["#FF0000", "#0000FF", "#808080"]
    for hex_val in hex_samples:
        rgb_value = hex_to_css(hex_val)
        print(f"'{hex_val}': {rgb_value}")