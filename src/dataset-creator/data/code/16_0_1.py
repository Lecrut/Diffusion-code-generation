import json
def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
def rgb_to_name(r, g, b):
    if r == 255 and g == 0 and b == 0:
        return "Red"
    elif r == 0 and g == 255 and b == 0:
        return "Green"
    elif r == 0 and g == 0 and b == 255:
        return "Blue"
    elif r == 255 and g == 255 and b == 0:
        return "Yellow"
    elif r == 255 and g == 165 and b == 0:
        return "Orange"
    elif r == 255 and g == 255 and b == 255:
        return "Cyan"
    elif r == 128 and g == 128 and b == 128:
        return "Gray"
    elif r == 0 and g == 0 and b == 0:
        return "Black"
    elif r == 255 and g == 0 and b == 255:
        return "Magenta"
    else:
        return "Custom"
def map_color_codes(color_data):
    color_map = {}
    for code, name in color_data.items():
        if isinstance(code, str) and code.startswith('#'):
            rgb = hex_to_rgb(code)
            name = rgb_to_name(*rgb)
        elif isinstance(code, tuple) and len(code) == 3:
            r, g, b = code
            name = rgb_to_name(r, g, b)
        else:
            name = "Unknown Format"
        color_map[code] = name
    return color_map
if __name__ == '__main__':
    sample_colors = {
        "#FF0000": "Red",
        "#00FF00": "Green",
        "#0000FF": "Blue",
        "#FFFF00": "Yellow",
        "#808080": "Gray",
        "#000000": "Black",
        "#FF00FF": "Magenta",
        "#00FFFF": "Cyan",
        "#123456": "Custom"
    }
    mapped_colors = map_color_codes(sample_colors)
    print(json.dumps(mapped_colors, indent=4))