favorite_colors = set()

def add_color(color):
    favorite_colors.add(color)

def check_colors(*colors_to_check):
    return all((color in favorite_colors for color in colors_to_check))

if __name__ == '__main__':
    add_color('Red')
    add_color('Blue')
    add_color('Green')
    print(check_colors('Red', 'Blue'))
    print(check_colors('Yellow'))