def css_to_hex(color_name):
    color_map = {
        "red": "#ff0000",
        "blue": "#0000ff",
        "green": "#008000",
        "yellow": "#ffff00",
        "black": "#000000",
        "white": "#ffffff",
        "gray": "#808080"
    }
    return color_map.get(color_name.lower(), "Color not found")
def hex_to_css(hex_code):
    hex_map = {
        "#ff0000": "red",
        "#0000ff": "blue",
        "#008000": "green",
        "#ffff00": "yellow",
        "#000000": "black",
        "#ffffff": "white",
        "#808080": "gray"
    }
    return hex_map.get(hex_code, "Hex not found")
if __name__ == '__main__':
    color_names = ["red", "blue", "green", "yellow", "black", "white", "gray"]
    print("--- CSS Color Name to Hex Code Mapping ---")
    for name in color_names:
        hex_code = css_to_hex(name)
        print(f"{name.capitalize()}: {hex_code}")
    print("\n--- Inverse Mapping (Hex Code to CSS Name) ---")
    hex_codes = ["#ff0000", "#0000ff", "#008000", "#ffff00", "#000000", "#ffffff", "#808080"]
    for hex_code in hex_codes:
        css_name = hex_to_css(hex_code)
        print(f"{hex_code}: {css_name}")