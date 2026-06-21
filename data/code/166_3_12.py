colors = set()

def add_color(color):
    colors.add(color)

def has_color(color):
    return color in colors
if __name__ == '__main__':
    add_color('red')
    add_color('blue')
    add_color('green')
    print(has_color('red'))
    print(has_color('yellow'))