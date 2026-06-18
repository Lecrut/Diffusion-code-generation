def css_to_hex_map():
    color_map = {
        "red": "#ff0000",
        "blue": "#0000ff",
        "green": "#008000",
        "yellow": "#ffff00",
        "black": "#000000",
        "white": "#ffffff",
        "gray": "#808080"
    }
    hex_to_css_map = {
        "#ff0000": "red",
        "#0000ff": "blue",
        "#008000": "green",
        "#ffff00": "yellow",
        "#000000": "black",
        "#ffffff": "white",
        "#808080": "gray"
    }
    print("CSS Color Name to Hex Code Mapping:")
    for css, hex in color_map.items():
        print(f"{css}: {hex}")
    print("\nHex Code to CSS Name Mapping (Inverse):")
    for hex_code, css_name in hex_to_css_map.items():
        print(f"{hex_code}: {css_name}")
if __name__ == '__main__':
    css_to_hex_map()