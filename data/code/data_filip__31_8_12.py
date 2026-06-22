def hex_to_decimal_map(hex_colors):
    return {color: int(color.lstrip('#'), 16) for color in hex_colors}

if __name__ == '__main__':
    sample_hex_colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#000000', '#FFFFFF']
    result = hex_to_decimal_map(sample_hex_colors)
    print(result)