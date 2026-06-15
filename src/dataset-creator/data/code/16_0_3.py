import json
def hex_to_rgb(hex_code):
    if len(hex_code) != 6:
        raise ValueError("Invalid hex code length")
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return (r, g, b)
def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"
def get_color_name(rgb):
    if 0 <= rgb[0] <= 255 and 0 <= rgb[1] <= 255 and 0 <= rgb[2] <= 255:
        r, g, b = rgb
        if r > 200 and g < 50 and b < 50:
            return "dark red"
        elif r < 50 and g > 200 and b < 50:
            return "dark green"
        elif r < 50 and g < 50 and b > 200:
            return "dark blue"
        elif r > 200 and g > 200 and b < 50:
            return "orange"
        elif r > 150 and g > 150 and b < 100:
            return "red"
        elif r < 100 and g > 150 and b < 100:
            return "green"
        elif r < 100 and g < 100 and b > 150:
            return "blue"
        elif r > 200 and g > 100 and b < 100:
            return "magenta"
        elif r > 100 and g > 200 and b < 100:
            return "cyan"
        else:
            return "gray/other"
    return "invalid_rgb"
def map_color_codes(color_map):
    color_names = {}
    for code, name in color_map.items():
        if isinstance(code, str):
            try:
                if code.startswith('#'):
                    hex_val = code[1:]
                    rgb = hex_to_rgb(hex_val)
                    color_names[code] = get_color_name(rgb)
                elif code.startswith('rgb'):
                    parts = code.split(',')
                    if len(parts) == 3:
                        r, g, b = map(int, [p.strip() for p in parts])
                        rgb_tuple = (r, g, b)
                        color_names[code] = get_color_name(rgb_tuple)
                    else:
                        color_names[code] = "invalid_rgb_format"
                else:
                    color_names[code] = "unsupported_format"
            except ValueError:
                color_names[code] = "error_parsing"
        else:
            color_names[code] = name
    return color_names
if __name__ == '__main__':
    sample_data = {
        "#FF0000": "Red",
        "#00FF00": "Green",
        "#0000FF": "Blue",
        "#FFFF00": "Yellow",
        "rgb(255, 0, 0)": "Red_RGB",
        "rgb(0, 255, 0)": "Green_RGB",
        "rgb(0, 0, 255)": "Blue_RGB",
        "#AABBCC": "Custom_Hex",
        "rgb(10, 10, 10)": "Dark_Gray_RGB"
    }
    result = map_color_codes(sample_data)
    print(json.dumps(result, indent=4))