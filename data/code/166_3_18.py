FAVORITE_COLORS = set()

def add_color(color):
    FAVORITE_COLORS.add(color)

def check_colors(*colors_to_check):
    return all((color in FAVORITE_COLORS for color in colors_to_check))

if __name__ == '__main__':
    add_color('Red')
    add_color('Blue')
    add_color('Green')
    print(check_colors('Red', 'Blue'))
    print(check_colors('Yellow'))