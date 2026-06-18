import os
def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    if len(hex_code) != 6:
        return None
    try:
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        return (r, g, b)
    except ValueError:
        return None
def rgb_to_name(r, g, b):
    if r is None or g is None or b is None:
        return "Invalid Color"
    if r > 200 and g < 50 and b < 50:
        return "Dark Red"
    elif r < 50 and g > 200 and b < 50:
        return "Dark Green"
    elif r < 50 and g < 50 and b > 200:
        return "Dark Blue"
    elif r > 200 and g > 200 and b < 50:
        return "Orange"
    elif r > 200 and g < 200 and b < 50:
        return "Red"
    elif r < 50 and g > 200 and b > 200:
        return "Cyan"
    else:
        return f"RGB({r}, {g}, {b})"
def read_and_print_colors(filepath):
    try:
        with open(filepath, 'r') as f:
            hex_codes = [line.strip() for line in f if line.strip()]
        for hex_code in hex_codes:
            rgb = hex_to_rgb(hex_code)
            if rgb:
                color_name = rgb_to_name(*rgb)
                print(f"Hex: {hex_code} -> Name: {color_name}")
            else:
                print(f"Error processing hex code: {hex_code}")
    except FileNotFoundError:
        print(f"Error: File not found at path: {filepath}")
    except IOError as e:
        print(f"Error reading file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    sample_data = [
        "#FF0000",       
        "#00FF00",         
        "#0000FF",        
        "#FFFF00",          
        "#000000",         
        "#1A2B3C"                                                    
    ]
    sample_filename = "colors.txt"
    try:
        with open(sample_filename, 'w') as f:
            for code in sample_data:
                f.write(code + "\n")
        read_and_print_colors(sample_filename)
    except IOError as e:
        print(f"Setup error: Could not write sample data to {sample_filename}: {e}")