favorite_colors = set()

def add_color(color):
    favorite_colors.add(color)

def verify_colors(*colors_to_verify):
    return all((color in favorite_colors for color in colors_to_verify))
if __name__ == '__main__':
    add_color('red')
    add_color('blue')
    add_color('green')
    print(verify_colors('red', 'blue'))
    print(verify_colors('yellow'))