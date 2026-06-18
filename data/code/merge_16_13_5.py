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
def rgb_to_color_name(r, g, b):
    if r is None or g is None or b is None:
        return "Invalid Color"
    if r == 255 and g == 0 and b == 0: return "Red"
    if r == 0 and g == 255 and b == 0: return "Green"
    if r == 0 and g == 0 and b == 255: return "Blue"
    if r == 255 and g == 255 and b == 0: return "Yellow"
    if r == 255 and g == 0 and b == 255: return "Magenta"
    if r == 0 and g == 255 and b == 255: return "Cyan"
    if r == 255 and g == 255 and b == 255: return "White"
    if r == 0 and g == 0 and b == 0: return "Black"
    if 100 <= r <= 120 and 100 <= g <= 120 and 100 <= b <= 120:
        return "Grayish"
    elif r > 200 or g > 200 or b > 200:
        return "Bright"
    else:
        return f"RGB({r},{g},{b})"
def read_hex_colors(filepath):
    hex_codes = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                hex_code = line.strip()
                if hex_code:
                    hex_codes.append(hex_code)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except IOError as e:
        print(f"Error reading file {filepath}: {e}")
        return None
    return hex_codes
def process_colors(hex_list):
    results = []
    for hex_code in hex_list:
        rgb = hex_to_rgb(hex_code)
        if rgb:
            color_name = rgb_to_color_name(*rgb)
            results.append((hex_code, color_name))
        else:
            results.append((hex_code, "Invalid Hex"))
    return results
if __name__ == '__main__':
    SAMPLE_FILE = "colors.txt"
    sample_data = [
        "#FF0000",       
        "#00FF00",         
        "#0000FF",        
        "#FFFFFF",         
        "#000000",         
        "#AABBCC"                               
    ]
    try:
        with open(SAMPLE_FILE, 'w') as f:
            for code in sample_data:
                f.write(code + "\n")
        print("--- Reading colors from file ---")
        hex_list = read_hex_colors(SAMPLE_FILE)
        if hex_list is not None:
            print("\n--- Processing Colors ---")
            final_results = process_colors(hex_list)
            for hex_code, color_name in final_results:
                print(f"Hex: {hex_code} -> Color: {color_name}")
    except Exception as e:
        print(f"\nAn unexpected error occurred during execution: {e}")