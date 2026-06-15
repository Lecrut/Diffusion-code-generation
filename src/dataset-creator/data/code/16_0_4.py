import json
def hex_to_rgb(hex_code):
    if len(hex_code) != 6:
        return None
    try:
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        return (r, g, b)
    except ValueError:
        return None
def rgb_to_name(r, g, b):
    if r is None or g is None or b is None:
        return "Invalid RGB"
    if r > 200 and g < 50 and b < 50:
        return "Dark Red"
    elif r < 50 and g > 200 and b < 50:
        return "Dark Green"
    elif r < 50 and g < 50 and b > 200:
        return "Dark Blue"
    elif r > 200 and g > 200 and b < 50:
        return "Orange"
    elif r > 150 and g > 150 and b < 100:
        return "Red"
    elif r > 100 and g < 100 and b < 100:
        return "Teal"
    elif r < 100 and g > 150 and b < 100:
        return "Cyan"
    elif r < 100 and g < 100 and b > 150:
        return "Blue"
    elif r > 200 and g > 100 and b < 100:
        return "Magenta"
    else:
        return "Custom Color"
def map_color_codes(color_dict):
    color_map = {}
    for code, name in color_dict.items():
        if isinstance(code, str):
            if code.startswith('#'):
                rgb = hex_to_rgb(code)
                if rgb:
                    name_result = rgb_to_name(*rgb)
                    color_map[code] = name_result
                else:
                    color_map[code] = "Invalid Hex"
            elif code.startswith('rgb'):
                try:
                    parts = code.split(',')
                    if len(parts) == 3:
                        r, g, b = map(int, parts)
                        name_result = rgb_to_name(r, g, b)
                        color_map[code] = name_result
                    else:
                        color_map[code] = "Invalid RGB Format"
                except ValueError:
                    color_map[code] = "Invalid RGB Values"
            else:
                color_map[code] = "Unknown Format"
        else:
            color_map[code] = "Not a string code"
    return color_map
if __name__ == '__main__':
    sample_colors = {
        "#FF0000": "Red",
        "#00FF00": "Green",
        "#0000FF": "Blue",
        "#FFFF00": "Yellow",
        "#00FFFF": "Cyan",
        "rgb(255, 0, 0)": "Red",
        "rgb(0, 255, 0)": "Green",
        "rgb(10, 10, 30)": "Dark Blue",
        "#AABBCC": "Custom Color"
    }
    result_map = map_color_codes(sample_colors)
    print(json.dumps(result_map, indent=4))