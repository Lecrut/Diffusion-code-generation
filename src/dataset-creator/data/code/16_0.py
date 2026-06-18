import json
def hex_to_rgb(hex_code):
    if len(hex_code) != 6:
        raise ValueError("Invalid hex code length")
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return r, g, b
def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"
def get_color_name(rgb):
    if rgb == (255, 0, 0):
        return "Red"
    elif rgb == (0, 0, 255):
        return "Blue"
    elif rgb == (0, 255, 0):
        return "Green"
    elif rgb == (255, 255, 0):
        return "Yellow"
    elif rgb == (255, 165, 0):
        return "Orange"
    elif rgb == (255, 255, 255):
        return "White"
    elif rgb == (0, 0, 0):
        return "Black"
    elif rgb == (128, 0, 128):
        return "Purple"
    else:
        return "Custom"
def map_color_codes(color_data):
    color_map = {}
    for code, name in color_data.items():
        if isinstance(code, str):
            try:
                if code.startswith('#'):
                    hex_val = code
                    r, g, b = hex_to_rgb(hex_val)
                    rgb_tuple = (r, g, b)
                else:
                    parts = code.split(',')
                    if len(parts) == 3:
                        r, g, b = map(int, parts)
                        rgb_tuple = (r, g, b)
                    else:
                        continue
                name = get_color_name(rgb_tuple)
                color_map[code] = name
            except ValueError:
                color_map[code] = "Error Parsing"
        else:
            color_map[code] = name
    return color_map
if __name__ == '__main__':
    sample_colors = {
        "#FF0000": "Red",
        "0000FF": "Blue",
        "00FF00": "Green",
        "#FFFF00": "Yellow",
        "FFFFFF": "White",
        "#000000": "Black",
        "#800080": "Purple",
        "255,165,0": "Orange"
    }
    color_names = map_color_codes(sample_colors)
    print(json.dumps(color_names, indent=4))