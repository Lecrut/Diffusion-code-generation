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
        if not isinstance(hex_code, str) or len(hex_code) < 7:
            raise ValueError("Invalid hex code format")
        rgb = hex_to_rgb(hex_code)
        name = rgb_to_name(*rgb)
        return name
    except ValueError as e:
        return f"Error processing {hex_code}: {e}"
    except Exception as e:
        return f"An unexpected error occurred for {hex_code}: {e}"
if __name__ == '__main__':
    hex_list = [
        "#FF0000",
        "#00FF00",
        "#0000FF",
        "#FFFFFF",
        "#1A1A1A",
        "#000000",
        "invalid_code",
        "#AABBCC"
    ]
    results = {}
    for hex_code in hex_list:
        name = get_color_name(hex_code)
        results[hex_code] = name
    for code, name in results.items():
        print(f"{code}: {name}")