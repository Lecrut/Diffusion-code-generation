colors = set()

def add_color(color):
    colors.add(color)

def check_colors(*colors_to_check):
    return all((color in colors for color in colors_to_check))
if __name__ == '__main__':
    add_color('red')
    add_color('green')
    add_color('blue')
    print(check_colors('red', 'green'))
    print(check_colors('yellow'))