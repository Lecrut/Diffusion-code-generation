import requests
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
def rgb_to_name(r, g, b):
    if r > 200 and g < 50 and b < 50:
        return "Red"
    elif r < 50 and g > 200 and b < 50:
        return "Green"
    elif r < 50 and g < 50 and b > 200:
        return "Blue"
    elif r > 200 and g > 200 and b < 50:
        return "Orange"
    elif r > 150 and g > 150 and b > 150:
        return "Gray/Neutral"
    else:
        return "Custom/Unknown"
def hex_to_color_name(hex_codes):
    color_names = []
    for hex_code in hex_codes:
        try:
            if not isinstance(hex_code, str) or len(hex_code) < 7:
                raise ValueError("Invalid hex code format")
            rgb = hex_to_rgb(hex_code)
            name = rgb_to_name(*rgb)
            color_names.append(name)
        except ValueError as e:
            color_names.append(f"Error: {e}")
        except Exception as e:
            color_names.append(f"Unexpected Error: {e}")
    return color_names
if __name__ == '__main__':
    sample_hex_codes = [
        "#FF0000",
        "#00FF00",
        "#0000FF",
        "#FFFFFF",
        "#1A1A1A",
        "#A3A3A3",
        "#FF6347",
        "invalid_code",
        "#12345678"
    ]
    results = hex_to_color_name(sample_hex_codes)
    for hex_code, color_name in zip(sample_hex_codes, results):
        print(f"Hex: {hex_code:<12} -> Name: {color_name}")