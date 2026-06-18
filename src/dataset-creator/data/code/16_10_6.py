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
        return "Invalid Hex Code"
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
        (255, 255, 0): 'LightYellow'
    }
    if rgb in color_map:
        return color_map[rgb]
    else:
        return "Color Not Found"
if __name__ == '__main__':
    hex_colors = [
        "#FF0000",
        "#00FF00",
        "#0000FF",
        "#FFFFFF",
        "#000000",
        "#FFA500",
        "#800080"
    ]
    print(f"Mapping results for sample colors:")
    for hex_code in hex_colors:
        color_name = hex_to_color_name(hex_code)
        print(f"{hex_code}: {color_name}")