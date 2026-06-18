import requests
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
def rgb_to_name(r, g, b):
    if r > 200 and g < 50 and b < 50:
        return "Dark Red"
    elif r > 150 and g > 150 and b < 50:
        return "Orange"
    elif r < 50 and g > 150 and b < 50:
        return "Green"
    elif r < 50 and g < 50 and b > 150:
        return "Blue"
    elif r > 200 and g > 200 and b < 100:
        return "Purple"
    else:
        return "Custom Color"
def get_color_name(hex_code):
    try:
        rgb = hex_to_rgb(hex_code)
        name = rgb_to_name(*rgb)
        return name
    except ValueError:
        return "Invalid Hex Code Format"
    except Exception:
        return "Error Processing Color"
if __name__ == '__main__':
    hex_list = [
        "#FF0000",
        "#00FF00",
        "#0000FF",
        "#FFFFFF",
        "#1A1A1A",
        "#800080",
        "invalid-hex",
        "#AABBCC"
    ]
    results = {}
    for hex_code in hex_list:
        try:
            color_name = get_color_name(hex_code)
            results[hex_code] = color_name
        except Exception as e:
            results[hex_code] = f"Critical Error: {e}"
    for hex_code, name in results.items():
        print(f"{hex_code}: {name}")