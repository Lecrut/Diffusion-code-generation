favorite_colors = set()

def add_color(color):
    favorite_colors.add(color)

def check_color_presence(*colors_to_check):
    return all((color in favorite_colors for color in colors_to_check))
if __name__ == '__main__':
    add_color('red')
    add_color('blue')
    add_color('green')
    print(check_color_presence('red', 'blue'))
    print(check_color_presence('yellow'))