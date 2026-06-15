import sys
def hex_to_color_name(hex_code):
    hex_code = hex_code.lstrip('#')
    if len(hex_code) != 6:
        return "Invalid Hex Code Length"
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    rgb = (r, g, b)
    color_map = {
        (0, 0, 0): 'Black',
        (255, 0, 0): 'Red',
        (255, 165, 0): 'Orange',
        (255, 255, 0): 'Yellow',
        (0, 255, 0): 'Green',
        (0, 128, 0): 'DarkGreen',
        (0, 0, 255): 'Blue',
        (75, 0, 130): 'MidnightBlue',
        (138, 43, 226): 'Violet',
        (255, 255, 255): 'White',
        (255, 192, 203): 'Pink',
        (255, 105, 180): 'Coral',
        (128, 0, 128): 'Purple',
        (255, 0, 128): 'Magenta',
    }
    if rgb in color_map:
        return color_map[rgb]
    else:
        return f"RGB({r}, {g}, {b})"
if __name__ == '__main__':
    test_colors = [
        "#FF0000",
        "#0000FF",
        "#00FF00",
        "#000000",
        "#FFA500",
        "#800080",
        "#FFFFFF",
        "#123456"
    ]
    print("--- Hex to Color Mapping ---")
    for color in test_colors:
        name = hex_to_color_name(color)
        print(f"Hex: {color} -> Name: {name}")