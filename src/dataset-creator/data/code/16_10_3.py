import sys
def hex_to_color_name(hex_code):
    hex_code = hex_code.lstrip('#')
    if len(hex_code) != 6:
        return "Invalid Hex Code Length"
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    rgb = (r, g, b)
    colors = {
        (255, 0, 0): 'Red',
        (255, 165, 0): 'Orange',
        (255, 255, 0): 'Yellow',
        (0, 0, 255): 'Blue',
        (0, 255, 0): 'Green',
        (0, 255, 255): 'Cyan',
        (128, 0, 128): 'Purple',
        (255, 0, 255): 'Magenta',
        (255, 255, 255): 'White',
        (0, 0, 0): 'Black'
    }
    if rgb in colors:
        return colors[rgb]
    else:
        return f"RGB({r}, {g}, {b})"
if __name__ == '__main__':
    hex_colors = [
        "#FF0000",
        "#00FF00",
        "#0000FF",
        "#FFFF00",
        "#000000",
        "#FFFFFF",
        "#800080"
    ]
    print("Hex Color Mapping Results:")
    for hex_code in hex_colors:
        color_name = hex_to_color_name(hex_code)
        print(f"{hex_code}: {color_name}")