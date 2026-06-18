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
def color_map_lookup(color_data):
    color_names = {}
    for hex_code, name in color_data.items():
        if hex_code.startswith('#'):
            rgb = hex_to_rgb(hex_code)
            name = rgb_to_name(*rgb)
        elif 'rgb' in hex_code:
            try:
                r, g, b = map(int, hex_code.split(','))
                name = rgb_to_name(r, g, b)
            except ValueError:
                name = "Invalid RGB"
        else:
            name = name
        color_names[hex_code] = name
    return color_names
if __name__ == '__main__':
    sample_colors = {
        "#FF0000": "Red",
        "#00FF00": "Green",
        "#0000FF": "Blue",
        "#FFFF00": "Yellow",
        "#808080": "Gray",
        "#000000": "Black",
        "rgb(255, 0, 0)": "Red",
        "rgb(0, 255, 0)": "Green",
        "rgb(100, 100, 100)": "Gray",
        "#AABBCC": "Custom"
    }
    result = color_map_lookup(sample_colors)
    print(json.dumps(result, indent=4))