import matplotlib.colors as mcolors
def hex_to_name(hex_code):
    try:
        hex_code = hex_code.lstrip('#')
        if len(hex_code) != 6:
            raise ValueError("Invalid hex code length")
        rgb = mcolors.to_rgb(hex_code)
        return mcolors.color_name(rgb)
    except ValueError as e:
        return f"Error processing {hex_code}: {e}"
    except Exception as e:
        return f"An unexpected error occurred for {hex_code}: {e}"
if __name__ == '__main__':
    hex_colors = [
        "#FF0000",
        "#00FF00",
        "#0000FF",
        "#FFFF00",
        "#123456",
        "invalid_code",
        "#GGRRBB"
    ]
    results = []
    for hex_code in hex_colors:
        color_name = hex_to_name(hex_code)
        results.append((hex_code, color_name))
    for hex_code, name in results:
        print(f"Hex: {hex_code} -> Name: {name}")