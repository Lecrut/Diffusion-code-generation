def color_to_name(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 6:
        return "Invalid Hex Code"
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    rgb = (r, g, b)
    if rgb == (255, 0, 0):
        return "Red"
    elif rgb == (0, 255, 0):
        return "Green"
    elif rgb == (0, 0, 255):
        return "Blue"
    elif rgb == (255, 255, 0):
        return "Yellow"
    elif rgb == (255, 165, 0):
        return "Orange"
    elif rgb == (75, 0, 130):
        return "Midnight Blue"
    elif rgb == (128, 0, 128):
        return "Purple"
    elif rgb == (0, 255, 255):
        return "Cyan"
    elif rgb == (255, 255, 255):
        return "White"
    elif rgb == (0, 0, 0):
        return "Black"
    else:
        return "Custom Color"
if __name__ == '__main__':
    colors_to_test = [
        "#FF0000",
        "#00FF00",
        "#0000FF",
        "#FFFF00",
        "#FFA500",
        "#1A8B45",
        "#482C60",
        "#00FFFF",
        "#FFFFFF",
        "#000000",
        "#123456"
    ]
    for color in colors_to_test:
        name = color_to_name(color)
        print(f"Hex: {color} -> Name: {name}")