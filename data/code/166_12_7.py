FAVORITE_COLORS = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF', 'yellow': '#FFFF00', 'purple': '#800080', 'orange': '#FFA500', 'pink': '#FFC0CB', 'brown': '#964B00'}

def get_hex_code(color_name):
    return FAVORITE_COLORS.get(color_name, None)
if __name__ == '__main__':
    print(get_hex_code('red'))
    print(get_hex_code('green'))
    print(get_hex_code('blue'))
    print(get_hex_code('yellow'))
    print(get_hex_code('purple'))
    print(get_hex_code('orange'))
    print(get_hex_code('pink'))
    print(get_hex_code('brown'))
    print(get_hex_code('black'))