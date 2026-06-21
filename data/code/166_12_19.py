favorite_colors = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF', 'yellow': '#FFFF00', 'purple': '#800080', 'orange': '#FFA500', 'pink': '#FFC0CB', 'brown': '#964B00'}

def validate_color(color_name):
    if not isinstance(color_name, str) or color_name.strip() == '':
        raise ValueError('Invalid color name')
    return color_name.lower()

def get_hex_code(color_name):
    valid_color = validate_color(color_name)
    return favorite_colors.get(valid_color, None)
if __name__ == '__main__':
    print(get_hex_code('red'))
    print(get_hex_code('green'))
    print(get_hex_code('blue'))
    print(get_hex_code('yellow'))
    print(get_hex_code('purple'))
    print(get_hex_code('orange'))
    print(get_hex_code('pink'))
    print(get_hex_code('brown'))
    print(get_hex_code('cyan'))