def is_valid_web_color(color_name):
    valid_colors = {'red', 'blue', 'green', 'yellow', 'black', 'white', 'cyan', 'magenta', 'yellow', 'gray'}
    return color_name in valid_colors
if __name__ == '__main__':
    print(is_valid_web_color('red'))
    print(is_valid_web_color('purple'))