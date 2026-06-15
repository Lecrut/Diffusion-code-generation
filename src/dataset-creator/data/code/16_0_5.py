import json
def hex_to_rgb(hex_code):
    if len(hex_code) != 7:
        return None
    try:
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        return (r, g, b)
    except ValueError:
        return None
def rgb_to_name(r, g, b):
    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        return "Invalid RGB"
    if r > 180 and g < 50 and b < 50:
        return "Dark Red"
    elif r > 200 and g > 150 and b < 50:
        return "Orange"
    elif r < 50 and g > 150 and b < 50:
        return "Dark Cyan"
    elif r < 50 and g < 150 and b > 150:
        return "Dark Blue"
    elif r > 150 and g > 150 and b < 50:
        return "Purple"
    elif r > 200 and g < 100 and b < 100:
        return "Maroon"
    else:
        return "Custom Color"
def map_color_codes(color_data):
    color_map = {}
    for code, name in color_data.items():
        if isinstance(code, str):
            if code.startswith('#'):
                rgb = hex_to_rgb(code)
                if rgb:
                    name = rgb_to_name(*rgb)
                color_map[code] = name
            elif code.startswith('rgb'):
                try:
                    parts = code.split(',')
                    if len(parts) == 3:
                        r, g, b = map(int, parts)
                        name = rgb_to_name(r, g, b)
                        color_map[code] = name
                    else:
                        color_map[code] = "Invalid RGB Format"
                except ValueError:
                    color_map[code] = "Invalid RGB Values"
            else:
                color_map[code] = "Unknown Format"
        else:
            color_map[code] = name
    return color_map
if __name__ == '__main__':
    sample_colors = {
        "#FF0000": "Red",
        "#00FF00": "Green",
        "#0000FF": "Blue",
        "rgb(255, 0, 0)": "Red (RGB)",
        "rgb(0, 255, 0)": "Green (RGB)",
        "#800080": "Purple",
        "rgb(128, 128, 128)": "Gray (RGB)"
    }
    result_map = map_color_codes(sample_colors)
    print(json.dumps(result_map, indent=4))