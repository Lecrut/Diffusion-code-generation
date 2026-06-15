def hex_to_name(hex_color):
    hex_color = hex_color.lower()
    if len(hex_color) != 6:
        return "Invalid Hex"
    try:
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
    except ValueError:
        return "Invalid Hex"
    rgb = (r, g, b)
    color_map = {
        (255, 0, 0): "Red",
        (255, 165, 0): "Orange",
        (255, 255, 0): "Yellow",
        (0, 255, 0): "Green",
        (0, 128, 0): "DarkGreen",
        (0, 0, 255): "Blue",
        (75, 0, 130): "MidnightBlue",
        (138, 43, 226): "Violet",
        (255, 255, 255): "White",
        (255, 255, 0): "LightYellow",
        (255, 192, 203): "Pink",
        (255, 105, 180): "Pink",
    }
    if rgb in color_map:
        return color_map[rgb]
    else:
        return f"RGB({r}, {g}, {b})"
if __name__ == '__main__':
    print(hex_to_name("#FF0000"))
    print(hex_to_name("#00FF00"))
    print(hex_to_name("#0000FF"))
    print(hex_to_name("#FFFFFF"))
    print(hex_to_name("#123456"))
    print(hex_to_name("#AABBCC"))
    print(hex_to_name("#FF1493"))