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
        (255, 192, 203): "Pink"
    }
    for key, name in color_map.items():
        if rgb == key:
            return name
    return "Unknown Color"
if __name__ == '__main__':
    print(color_to_name("#FFFFFF"))
    print(color_to_name("#000000"))
    print(color_to_name("#FF0000"))
    print(color_to_name("#00FF00"))
    print(color_to_name("#0000FF"))
    print(color_to_name("#128000"))
    print(color_to_name("#FFC0CB"))
    print(color_to_name("#A52A2A"))
    print(color_to_name("#102030"))