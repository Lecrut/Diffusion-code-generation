def css_to_hex(color_name):
    color_map = {
        "red": "#FF0000",
        "blue": "#0000FF",
        "green": "#008000",
        "yellow": "#FFFF00",
        "black": "#000000",
        "white": "#FFFFFF",
        "gray": "#808080"
    }
    return color_map.get(color_name.lower(), "Color not found")
def hex_to_css(hex_code):
    hex_map = {
        "#FF0000": "red",
        "#0000FF": "blue",
        "#008000": "green",
        "#FFFF00": "yellow",
        "#000000": "black",
        "#FFFFFF": "white",
        "#808080": "gray"
    }
    return hex_map.get(hex_code, "Hex not found")
if __name__ == '__main__':
    color1 = "red"
    hex1 = css_to_hex(color1)
    print(f"{color1} maps to {hex1}")
    color2 = "blue"
    hex2 = css_to_hex(color2)
    print(f"{color2} maps to {hex2}")
    color3 = "black"
    hex3 = css_to_hex(color3)
    print(f"{color3} maps to {hex3}")
    print("-" * 20)
    hex_input1 = "#FF0000"
    css_output1 = hex_to_css(hex_input1)
    print(f"{hex_input1} maps to {css_output1}")
    hex_input2 = "#0000FF"
    css_output2 = hex_to_css(hex_input2)
    print(f"{hex_input2} maps to {css_output2}")
    hex_input3 = "#808080"
    css_output3 = hex_to_css(hex_input3)
    print(f"{hex_input3} maps to {css_output3}")