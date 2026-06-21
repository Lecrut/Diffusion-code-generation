def hex_to_decimal(hex_str):
    return int(hex_str, 16)

COLOR_MAP = {
    'RED': '#FF0000',
    'GREEN': '#00FF00',
    'BLUE': '#0000FF',
    'BLACK': '#000000',
    'WHITE': '#FFFFFF',
    'YELLOW': '#FFFF00',
    'CYAN': '#00FFFF',
    'MAGENTA': '#FF00FF',
    'ORANGE': '#FFA500',
    'PURPLE': '#800080',
}

def map_colors_to_decimal():
    result = {}
    for name, hex_code in COLOR_MAP.items():
        clean_hex = hex_code.lstrip('#')
        result[name] = hex_to_decimal(clean_hex)
    return result

if __name__ == '__main__':
    mapped_colors = map_colors_to_decimal()
    for name, decimal_val in mapped_colors.items():
        print(f"{name}: {decimal_val}")