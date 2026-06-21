def hex_to_decimal(hex_code):
    return int(hex_code, 16)

COLOR_MAP = {
    '#FF0000': hex_to_decimal('#FF0000'),
    '#00FF00': hex_to_decimal('#00FF00'),
    '#0000FF': hex_to_decimal('#0000FF'),
    '#FFFF00': hex_to_decimal('#FFFF00'),
    '#00FFFF': hex_to_decimal('#00FFFF'),
    '#FF00FF': hex_to_decimal('#FF00FF'),
    '#000000': hex_to_decimal('#000000'),
    '#FFFFFF': hex_to_decimal('#FFFFFF')
}

def get_color_decimals():
    return COLOR_MAP

if __name__ == '__main__':
    results = get_color_decimals()
    for hex_val, dec_val in results.items():
        print(f"{hex_val}: {dec_val}")