import matplotlib.colors as mcolors
def hex_to_name(hex_code):
    try:
        hex_code = hex_code.lstrip('#')
        if len(hex_code) != 6:
            raise ValueError("Invalid hex code length")
        rgb = mcolors.to_rgb(hex_code)
        return mcolors.color_name(rgb)
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    hex_list = [
        "#FF0000",
        "#00FF00",
        "#0000FF",
        "#FFFFFF",
        "#000000",
        "#AABBCC",
        "invalid_hex",
        "#12345678"
    ]
    results = []
    for hex_code in hex_list:
        color_name = hex_to_name(hex_code)
        results.append((hex_code, color_name))
    for hex_code, color_name in results:
        print(f"Hex: {hex_code}, Name: {color_name}")