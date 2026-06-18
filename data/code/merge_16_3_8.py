import requests
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
def rgb_to_name(r, g, b):
    if r > 200 and g < 50 and b < 50:
        return "dark red"
    elif r < 50 and g > 200 and b < 50:
        return "dark green"
    elif r < 50 and g < 50 and b > 200:
        return "dark blue"
    elif r > 200 and g > 200 and b < 50:
        return "orange"
    elif r > 150 and g > 150 and b > 150:
        return "light gray"
    else:
        return "custom color"
def get_color_name(hex_code):
    try:
        rgb = hex_to_rgb(hex_code)
        r, g, b = rgb
        return rgb_to_name(r, g, b)
    except ValueError:
        return "Invalid Hex Code Format"
    except Exception:
        return "Unknown Error"
if __name__ == '__main__':
    hex_list = [
        "#FF0000",
        "#00FF00",
        "#0000FF",
        "#FFFFFF",
        "#123456",
        "#AABBCC",
        "invalid-code",
        "#100000"
    ]
    results = {}
    for hex_code in hex_list:
        color_name = get_color_name(hex_code)
        results[hex_code] = color_name
    for hex_code, name in results.items():
        print(f"Hex: {hex_code}, Name: {name}")