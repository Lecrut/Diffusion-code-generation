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
    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        colors = {
            (255, 0, 0): "Red",
            (255, 165, 0): "Orange",
            (255, 255, 0): "Yellow",
            (0, 255, 0): "Green",
            (0, 128, 0): "DarkGreen",
            (0, 0, 255): "Blue",
            (75, 0, 130): "MidnightBlue",
            (10, 10, 10): "gray",
            (255, 255, 255): "White",
            (255, 255, 0): "LightYellow",
            (255, 165, 0): "LightSalmon",
            (255, 105, 180): "Pink",
        }
        return colors.get((r, g, b), f"RGB({r},{g},{b})")
    return "Invalid RGB values"
def read_hex_colors(filepath):
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except IOError as e:
        print(f"Error reading file {filepath}: {e}")
        return None
def process_colors(hex_list):
    results = []
    for hex_code in hex_list:
        try:
            rgb = hex_to_rgb(hex_code)
            color_name = rgb_to_name(*rgb)
            results.append(f"{hex_code}: {color_name}")
        except ValueError as e:
            results.append(f"{hex_code}: Error - {e}")
    return results
if __name__ == '__main__':
    sample_filename = "colors.txt"
    sample_data = [
        "#FF0000",
        "#00FF00",
        "#0000FF",
        "#FFFF00",
        "#123456",
        "#AABBCC",
        "#112233"
    ]
    try:
        with open(sample_filename, 'w') as f:
            for code in sample_data:
                f.write(code + "\n")
    except IOError as e:
        print(f"Could not write sample data to {sample_filename}: {e}")
        exit(1)
    read_codes = read_hex_colors(sample_filename)
    if read_codes is not None:
        processed_output = process_colors(read_codes)
        for result in processed_output:
            print(result)