def hex_to_decimal_lookup(hex_colors):
    color_map = {
        "#FF0000": (255, 0, 0),
        "#00FF00": (0, 255, 0),
        "#0000FF": (0, 0, 255),
        "#FFFFFF": (255, 255, 255),
        "#000000": (0, 0, 0),
        "#FFFF00": (255, 255, 0),
        "#FF00FF": (255, 0, 255),
        "#00FFFF": (0, 255, 255),
        "#808080": (128, 128, 128),
        "#C0C0C0": (192, 192, 192),
    }
    result = {}
    for color in hex_colors:
        upper_color = color.upper()
        if upper_color in color_map:
            result[color] = color_map[upper_color]
        else:
            r = int(upper_color[1:3], 16)
            g = int(upper_color[3:5], 16)
            b = int(upper_color[5:7], 16)
            result[color] = (r, g, b)
    return result

if __name__ == '__main__':
    sample_colors = ["#FF0000", "#00FF00", "#123456", "#ABCDEF", "#000000"]
    conversions = hex_to_decimal_lookup(sample_colors)
    print(conversions)