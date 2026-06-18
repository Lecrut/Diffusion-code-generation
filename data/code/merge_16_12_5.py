def hex_to_name(hex_color):
    hex_color = hex_color.lower()
    if len(hex_color) != 6:
        return "Invalid Hex Color"
    try:
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
    except ValueError:
        return "Invalid Hex Color"
    rgb = (r, g, b)
    if rgb == (255, 0, 0):
        return "Red"
    elif rgb == (255, 165, 0):
        return "Orange"
    elif rgb == (255, 255, 0):
        return "Yellow"
    elif rgb == (0, 255, 0):
        return "Green"
    elif rgb == (0, 128, 0):
        return "DarkGreen"
    elif rgb == (0, 0, 255):
        return "Blue"
    elif rgb == (75, 0, 130):
        return "MidnightBlue"
    elif rgb == (128, 0, 128):
        return "Purple"
    elif rgb == (255, 0, 255):
        return "Magenta"
    elif rgb == (255, 255, 255):
        return "White"
    elif rgb == (255, 255, 0):
        return "LightYellow"
    elif rgb == (178, 34, 34):
        return "Tomato"
    elif rgb == (128, 128, 128):
        return "Gray"
    else:
        return "Custom RGB"
if __name__ == '__main__':
    print(hex_to_name("#FF0000"))
    print(hex_to_name("#00FF00"))
    print(hex_to_name("#0000FF"))
    print(hex_to_name("#FFFFFF"))
    print(hex_to_name("#800080"))
    print(hex_to_name("#123456"))
    print(hex_to_name("#FF8000"))
    print(hex_to_name("#A0A0A0"))
    print(hex_to_name("#FF00FF"))
    print(hex_to_name("#000000"))
    print(hex_to_name("#FFFF00"))