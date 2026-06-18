def color_name_to_hex(color_name):
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
def hex_to_color_name(hex_code):
    color_map = {
        "#FF0000": "red",
        "#0000FF": "blue",
        "#008000": "green",
        "#FFFF00": "yellow",
        "#000000": "black",
        "#FFFFFF": "white",
        "#808080": "gray"
    }
    return color_map.get(hex_code, "Hex not found")
if __name__ == '__main__':
    color1 = "red"
    hex1 = color_name_to_hex(color1)
    print(f"{color1} maps to: {hex1}")
    color2 = "blue"
    hex2 = color_name_to_hex(color2)
    print(f"{color2} maps to: {hex2}")
    color3 = "yellow"
    hex3 = color_name_to_hex(color3)
    print(f"{color3} maps to: {hex3}")
    print("-" * 20)
    hex_input1 = "#FF0000"
    name1 = hex_to_color_name(hex_input1)
    print(f"{hex_input1} maps to: {name1}")
    hex_input2 = "#0000FF"
    name2 = hex_to_color_name(hex_input2)
    print(f"{hex_input2} maps to: {name2}")
    hex_input3 = "#808080"
    name3 = hex_to_color_name(hex_input3)
    print(f"{hex_input3} maps to: {name3}")