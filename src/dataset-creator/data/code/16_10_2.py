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
        (255, 0, 0): 'Red',
        (0, 0, 255): 'Blue',
        (0, 255, 0): 'Green',
        (255, 255, 0): 'Yellow',
        (255, 0, 255): 'Magenta',
        (0, 255, 255): 'Cyan',
        (255, 255, 255): 'White',
        (0, 0, 0): 'Black',
        (255, 165, 0): 'Orange',
        (128, 0, 128): 'Purple',
        (0, 128, 0): 'Greenish',
    }
    if rgb in color_map:
        return color_map[rgb]
    else:
        return f"RGB({r}, {g}, {b})"
if __name__ == '__main__':
    hex_colors = [
        "#FF0000",
        "#0000FF",
        "#00FF00",
        "#FFFF00",
        "#FF00FF",
        "#00FFFF",
        "#FFFFFF",
        "#000000",
        "#FFA500",
        "#800080"
    ]
    print("Hex Color Mapping Results:")
    for hex_code in hex_colors:
        color_name = hex_to_color_name(hex_code)
        print(f"'{hex_code}' maps to: {color_name}")