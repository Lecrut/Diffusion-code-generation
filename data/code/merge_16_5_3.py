def color_to_name(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 6:
        return "Invalid Hex Code"
    try:
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
    except ValueError:
        return "Invalid Hex Code"
    rgb = (r, g, b)
    color_map = {
        (0, 0, 0): "Black",
        (255, 0, 0): "Red",
        (255, 165, 0): "Orange",
        (255, 255, 0): "Yellow",
        (0, 255, 0): "Green",
        (0, 128, 0): "DarkGreen",
        (0, 0, 255): "Blue",
        (75, 0, 130): "MidnightBlue",
        (138, 43, 226): "Violet",
        (255, 255, 255): "White"
    }
    for key, name in color_map.items():
        if key == rgb:
            return name
    return "Unknown Color"
if __name__ == '__main__':
    colors_to_test = [
        "#FF0000",
        "#00FF00",
        "#0000FF",
        "#000000",
        "#FFA500",
        "#800080",
        "#FFFFFF",
        "#123456"
    ]
    for color in colors_to_test:
        result = color_to_name(color)
        print(f"Hex: {color} -> Name: {result}")