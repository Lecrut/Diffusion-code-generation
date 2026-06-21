colors = set()

def add_color(color):
    if not isinstance(color, str) or not color:
        raise ValueError('Color must be a non-empty string')
    colors.add(color)

def check_colors(*colors_to_check):
    return all((color in colors for color in colors_to_check))
if __name__ == '__main__':
    try:
        add_color('red')
        add_color('blue')
        add_color('green')
        print(check_colors('red', 'blue'))
        print(check_colors('yellow'))
    except ValueError as e:
        print(e)