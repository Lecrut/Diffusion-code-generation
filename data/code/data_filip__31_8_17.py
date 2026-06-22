def hex_to_decimal_map(hex_codes):
    result = {}
    for key, hex_code in hex_codes.items():
        clean_hex = hex_code.lstrip('#')
        decimal_value = int(clean_hex, 16)
        result[key] = decimal_value
    return result

if __name__ == '__main__':
    hardcoded_hex_colors = {
        'red': '#FF0000',
        'green': '#00FF00',
        'blue': '#0000FF',
        'white': '#FFFFFF',
        'black': '#000000'
    }
    mapped_values = hex_to_decimal_map(hardcoded_hex_colors)
    print(mapped_values)