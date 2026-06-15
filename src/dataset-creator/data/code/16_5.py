def color_to_name(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 6:
        return "Invalid Hex Code"
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    rgb = (r, g, b)
    color_map = {
        (0, 0, 0): "Black",
        (255, 255, 255): "White",
        (255, 0, 0): "Red",
        (255, 165, 0): "Orange",
        (255, 255, 0): "Yellow",
        (0, 255, 0): "Green",
        (0, 128, 0): "DarkGreen",
        (0, 0, 255): "Blue",
        (75, 0, 130): "MidnightBlue",
        (128, 0, 128): "Purple",
    }
    for key, name in color_map.items():
        if rgb == key:
            return name
    return "Color Not Found"
if __name__ == '__main__':
    print(color_to_name("#FFFFFF"))
    print(color_to_name("#000000"))
    print(color_to_name("#FF0000"))
    print(color_to_name("#00FF00"))
    print(color_to_name("#128080"))
    print(color_to_name("#750080"))
    print(color_to_name("#AABBCC"))