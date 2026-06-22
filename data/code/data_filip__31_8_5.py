def hex_to_decimal(hex_string):
    return int(hex_string, 16)
HEX_PALETTE = {'FF0000': 'Red', '00FF00': 'Green', '0000FF': 'Blue', 'FFFFFF': 'White', '000000': 'Black', 'FFFF00': 'Yellow', 'FF00FF': 'Magenta', '00FFFF': 'Cyan'}
DECIMAL_PALETTE = {hex_code: hex_to_decimal(hex_code) for hex_code in HEX_PALETTE}

def get_decimal_colors():
    return DECIMAL_PALETTE
if __name__ == '__main__':
    result = get_decimal_colors()
    print(result)