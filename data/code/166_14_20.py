def is_valid_web_color(color_name):
    valid_colors = {'red', 'green', 'blue', 'yellow', 'black', 'white', 'cyan', 'magenta', 'purple', 'orange', 'brown'}
    return color_name in valid_colors
if __name__ == '__main__':
    print(is_valid_web_color('red'))
    print(is_valid_web_color('blue'))
    print(is_valid_web_color('black'))
    print(is_valid_web_color('white'))
    print(is_valid_web_color('gray'))
    print(is_valid_web_color('cyan'))
    print(is_valid_web_color('magenta'))
    print(is_valid_web_color('purple'))
    print(is_valid_web_color('orange'))
    print(is_valid_web_color('brown'))
    print(is_valid_web_color('pink'))