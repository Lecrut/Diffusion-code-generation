import os
def hex_to_color_name(hex_code):
    if len(hex_code) != 7 or not all(c in '0123456789abcdefABCDEF' for c in hex_code):
        return "Invalid Hex Code"
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    rgb_tuple = (r, g, b)
    if rgb_tuple == (255, 0, 0):
        return "Red"
    elif rgb_tuple == (0, 0, 255):
        return "Blue"
    elif rgb_tuple == (0, 255, 0):
        return "Green"
    elif rgb_tuple == (255, 255, 0):
        return "Yellow"
    elif rgb_tuple == (255, 165, 0):
        return "Orange"
    elif rgb_tuple == (128, 0, 128):
        return "Purple"
    else:
        return f"RGB({r},{g},{b})"
def process_color_file(filepath):
    try:
        with open(filepath, 'r') as f:
            hex_codes = [line.strip() for line in f if line.strip()]
            for hex_code in hex_codes:
                color_name = hex_to_color_name(hex_code)
                print(f"Hex: {hex_code} -> Color: {color_name}")
    except FileNotFoundError:
        print(f"Error: File not found at path: {filepath}")
    except IOError as e:
        print(f"Error reading file {filepath}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    sample_filename = "colors.txt"
    sample_data = [
        "#FF0000",       
        "#00FF00",         
        "#0000FF",        
        "#FFFF00",          
        "#800080"                           
    ]
    try:
        with open(sample_filename, 'w') as f:
            for code in sample_data:
                f.write(code + "\n")
        process_color_file(sample_filename)
    except IOError as e:
        print(f"Error writing sample data to {sample_filename}: {e}")