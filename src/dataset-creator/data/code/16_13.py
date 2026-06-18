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
def rgb_to_color_name(r, g, b):
    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        if r == 255 and g == 0 and b == 0:
            return "Red"
        elif r == 0 and g == 255 and b == 0:
            return "Green"
        elif r == 0 and g == 0 and b == 255:
            return "Blue"
        elif r == 255 and g == 255 and b == 0:
            return "Yellow"
        elif r == 255 and g == 0 and b == 255:
            return "Magenta"
        elif r == 0 and g == 255 and b == 255:
            return "Cyan"
        else:
            return f"RGB({r}, {g}, {b})"
    return "Invalid RGB values"
def read_hex_colors(filepath):
    color_codes = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                hex_code = line.strip()
                if hex_code:
                    color_codes.append(hex_code)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except IOError as e:
        print(f"Error reading file {filepath}: {e}")
        return None
    return color_codes
def process_colors(hex_list):
    results = []
    for hex_code in hex_list:
        try:
            rgb = hex_to_rgb(hex_code)
            color_name = rgb_to_color_name(*rgb)
            results.append((hex_code, color_name))
        except ValueError as e:
            results.append((hex_code, f"Error: {e}"))
    return results
if __name__ == '__main__':
    sample_filename = "colors.txt"
    sample_data = [
        "#FF0000",       
        "#00FF00",         
        "#0000FF",        
        "#FFFF00",          
        "#00FFFF",        
        "#FF00FF",           
        "#123456"                                                      
    ]
    try:
        with open(sample_filename, 'w') as f:
            for code in sample_data:
                f.write(code + '\n')
        print("--- Processing data from file ---")
        read_codes = read_hex_colors(sample_filename)
        if read_codes is not None:
            processed_results = process_colors(read_codes)
            for hex_code, color_name in processed_results:
                print(f"Hex: {hex_code} -> Color: {color_name}")
    except Exception as e:
        print(f"An unexpected error occurred during execution: {e}")