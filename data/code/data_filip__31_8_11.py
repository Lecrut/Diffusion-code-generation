def hex_to_decimal(hex_code):
    return int(hex_code, 16)
COLOR_MAP = {'#FF0000': (255, 0, 0), '#00FF00': (0, 255, 0), '#0000FF': (0, 0, 255), '#FFFFFF': (255, 255, 255), '#000000': (0, 0, 0)}

def convert_color(hex_code):
    hex_code = hex_code.lstrip('#')
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return (r, g, b)

def get_decimal_map():
    result = {}
    for hex_val, decimal_tuple in COLOR_MAP.items():
        r, g, b = decimal_tuple
        combined = r << 16 | g << 8 | b
        result[hex_val] = combined
    return result
if __name__ == '__main__':
    samples = ['#FF0000', '#00FF00', '#0000FF', '#FFFFFF', '#000000']
    converted_values = [convert_color(color) for color in samples]
    print(f'Direct Conversion: {converted_values}')
    decimal_map = get_decimal_map()
    mapped_values = [decimal_map[color] for color in samples]
    print(f'Mapped Decimal: {mapped_values}')
    print(f'First Color RGB: {converted_values[0]}')
    print(f'First Color Integer: {mapped_values[0]}')