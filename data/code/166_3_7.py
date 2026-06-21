COLOR_SET = set()

def add_color(color):
    COLOR_SET.add(color)

def check_colors(*colors_to_check):
    return all((color in COLOR_SET for color in colors_to_check))

if __name__ == '__main__':
    add_color('red')
    add_color('blue')
    add_color('green')
    print(check_colors('red', 'blue'))
    print(check_colors('yellow'))