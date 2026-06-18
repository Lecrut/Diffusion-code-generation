import sys
def hex_to_color_name(hex_code):
    hex_code = hex_code.lstrip('#')
    if len(hex_code) != 6:
        return "Invalid Hex Code Length"
    try:
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
    except ValueError:
        return "Invalid Hexadecimal Characters"
    rgb = (r, g, b)
    if rgb == (255, 0, 0):
        return "Red"
    elif rgb == (0, 0, 255):
        return "Blue"
    elif rgb == (0, 255, 0):
        return "Green"
    elif rgb == (255, 255, 0):
        return "Yellow"
    elif rgb == (255, 165, 0):
        return "Orange"
    elif rgb == (255, 255, 255):
        return "White"
    elif rgb == (0, 255, 255):
        return "Cyan"
    elif rgb == (128, 0, 128):
        return "Purple"
    elif rgb == (255, 0, 255):
        return "Magenta"
    elif rgb == (0, 0, 0):
        return "Black"
    else:
        return f"RGB({rgb[0]}, {rgb[1]}, {rgb[2]})"
if __name__ == '__main__':
    color_map = {
        "#FF0000": "Red",
        "#0000FF": "Blue",
        "#00FF00": "Green",
        "#FFFF00": "Yellow",
        "#FFA500": "Orange",
        "#FFFFFF": "White",
        "#000000": "Black",
        "#800080": "Purple",
        "#FF00FF": "Magenta"
    }
    test_colors = [
        "#FF0000",
        "#0000FF",
        "#00FF00",
        "#FFFFFF",
        "#000000",
        "#123456",
        "#AABBCC"
    ]
    print("--- Hardcoded Color Mapping ---")
    for color in test_colors:
        name = hex_to_color_name(color)
        print(f"Hex: {color} -> Name: {name}")