import os
def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    if len(hex_code) != 6:
        raise ValueError("Invalid hex code length")
    try:
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        return (r, g, b)
    except ValueError:
        raise ValueError("Invalid hexadecimal characters")
def rgb_to_name(r, g, b):
    if (r, g, b) == (255, 0, 0):
        return "Red"
    elif (r, g, b) == (0, 0, 255):
        return "Blue"
    elif (r, g, b) == (0, 255, 0):
        return "Green"
    elif (r, g, b) == (255, 255, 0):
        return "Yellow"
    elif (r, g, b) == (255, 0, 255):
        return "Magenta"
    elif (r, g, b) == (0, 255, 255):
        return "Cyan"
    elif (r, g, b) == (255, 255, 255):
        return "White"
    elif (r, g, b) == (0, 0, 0):
        return "Black"
    else:
        return f"RGB({r},{g},{b})"
def read_and_print_colors(filepath):
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
        for line in lines:
            hex_code = line.strip()
            if not hex_code:
                continue
            try:
                rgb = hex_to_rgb(hex_code)
                color_name = rgb_to_name(*rgb)
                print(f"Hex: {hex_code} -> Name: {color_name}")
            except ValueError as e:
                print(f"Error processing line '{hex_code}': {e}")
    except FileNotFoundError:
        print(f"Error: File not found at path: {filepath}")
    except IOError as e:
        print(f"Error reading file: {e}")
if __name__ == '__main__':
    sample_data = [
        "#FF0000",
        "#00FF00",
        "#0000FF",
        "#FFFFFF",
        "#000000",
        "#808080",
        "#123456"                                           
    ]
    sample_filename = "colors.txt"
    try:
        with open(sample_filename, 'w') as f:
            for code in sample_data:
                f.write(code + '\n')
        read_and_print_colors(sample_filename)
    except IOError as e:
        print(f"Fatal Error during file setup: {e}")