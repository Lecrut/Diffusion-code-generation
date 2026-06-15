import requests
def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    if len(hex_code) != 6:
        raise ValueError("Invalid hex code length")
    try:
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        return r, g, b
    except ValueError:
        raise ValueError("Invalid hexadecimal characters")
def rgb_to_name(r, g, b):
    if r > 200 and g < 50 and b < 50:
        return "Dark Red"
    elif r < 50 and g > 200 and b < 50:
        return "Dark Green"
    elif r < 50 and g < 50 and b > 200:
        return "Dark Blue"
    elif r > 200 and g > 200 and b < 50:
        return "Orange"
    elif r > 150 and g > 150 and b < 150:
        return "Light Red"
    elif r < 50 and g > 150 and b < 50:
        return "Light Green"
    elif r < 50 and g < 50 and b > 150:
        return "Light Blue"
    else:
        return "Custom Color"
def map_hex_to_name(hex_list):
    color_names = []
    for hex_code in hex_list:
        try:
            r, g, b = hex_to_rgb(hex_code)
            name = rgb_to_name(r, g, b)
            color_names.append((hex_code, name))
        except ValueError as e:
            color_names.append((hex_code, f"Error: {e}"))
    return color_names
if __name__ == '__main__':
    sample_hex_colors = [
        "#FF0000",       
        "#00FF00",         
        "#0000FF",        
        "#FFFFFF",         
        "#123456",                
        "#FF8800"              
        "#GG0000",
        "#123"
    ]
    results = map_hex_to_name(sample_hex_colors)
    for hex_code, color_name in results:
        print(f"Hex: {hex_code}, Name: {color_name}")