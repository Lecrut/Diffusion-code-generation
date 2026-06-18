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
        return "Invalid Color"
    if r > 200 and g < 50 and b < 50:
        return "Dark Red"
    elif r > 150 and g > 150 and b < 50:
        return "Orange"
    elif r < 50 and g > 150 and b < 50:
        return "Cyan"
    elif r < 50 and g < 50 and b > 150:
        return "Blue"
    elif r > 150 and g < 200 and b < 100:
        return "Purple"
    else:
        return "Custom Color"
def map_color_codes(color_data):
    color_map = {}
    for code, name in color_data.items():
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
                    parts = code.split('(')[1].split(')')[0].split(',')
                    if len(parts) == 3:
                        r, g, b = map(int, [p.strip() for p in parts])
                        name_result = rgb_to_name(r, g, b)
                        color_map[code] = name_result
                    else:
                        color_map[code] = "Invalid RGB Format"
                except Exception:
                    color_map[code] = "Invalid RGB"
            else:
                color_map[code] = "Unknown Format"
        else:
            color_map[code] = "Invalid Entry Type"
    return color_map
if __name__ == '__main__':
    sample_colors = {
        "#FF0000": "Red",
        "#00FF00": "Green",
        "#0000FF": "Blue",
        "#FFFF00": "Yellow",
        "rgb(255, 0, 0)": "Red",
        "rgb(0, 255, 0)": "Green",
        "rgb(10, 10, 10)": "Dark Gray",
        "#AABBCC": "Custom Color"
    }
    result_map = map_color_codes(sample_colors)
    print(json.dumps(result_map, indent=4))