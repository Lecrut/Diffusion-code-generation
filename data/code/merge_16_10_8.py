import sys
def hex_to_color_name(hex_code):
    hex_code = hex_code.lstrip('#')
    if len(hex_code) != 6:
        return "Invalid Hex Code"
    try:
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
    except ValueError:
        return "Invalid Hex Value"
    rgb = (r, g, b)
    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        if r == g and g == b:
            return "White" if r == 255 else "Black"
        elif r > 180 and g < 30 and b < 30:
            return "Dark Blue"
        elif r > 200 and g < 50 and b < 50:
            return "Dark Red"
        elif r > 180 and g > 180 and b < 30:
            return "Dark Cyan"
        elif r < 30 and g < 30 and b > 200:
            return "Dark Blue"
        elif r < 30 and g > 200 and b < 30:
            return "Dark Red"
        elif r < 30 and g < 30 and b < 30:
            return "Black"
        elif r > 200 and g > 180 and b < 30:
            return "Dark Red"
        elif r > 180 and g < 30 and b > 200:
            return "Dark Blue"
        elif r > 150 and g > 150 and b < 50:
            return "Dark Orange"
        elif r < 50 and g > 200 and b < 30:
            return "Dark Blue"
        elif r < 30 and g > 200 and b < 30:
            return "Dark Red"
        elif r < 30 and g < 30 and b > 200:
            return "Dark Blue"
        elif r > 180 and g > 150 and b < 50:
            return "Dark Red"
        elif r > 150 and g < 50 and b > 180:
            return "Dark Purple"
        elif r > 200 and g > 100 and b < 50:
            return "Dark Orange"
        else:
            if r > 220 and g > 220 and b > 220:
                return "Light Gray"
            elif r > 220 and g < 50 and b < 50:
                return "Dark Gray"
            elif r > 180 and g > 180 and b > 180:
                return "Light Gray"
            else:
                return "Custom Color"
    else:
        return "Invalid RGB Range"
if __name__ == '__main__':
    color_map = {
        "#FF0000": "Red",
        "#00FF00": "Green",
        "#0000FF": "Blue",
        "#FFFF00": "Yellow",
        "#FFA500": "Orange",
        "#800080": "Purple",
        "#000000": "Black",
        "#FFFFFF": "White",
        "#000000": "Black",
        "#808080": "Gray"
    }
    test_colors = [
        "#FF0000",
        "#00FF00",
        "#0000FF",
        "#AABBCC",
        "#123456",
        "#FFFFFF",
        "#112233"
    ]
    print("--- Hex to Color Name Mapping ---")
    for color in test_colors:
        name = hex_to_color_name(color)
        print(f"Hex: {color} -> Name: {name}")