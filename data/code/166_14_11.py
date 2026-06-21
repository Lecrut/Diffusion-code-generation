valid_web_colors = {'red', 'green', 'blue', 'yellow', 'black', 'white', 'cyan', 'magenta', 'orange', 'purple', 'pink', 'brown'}

def is_valid_web_color(color_name):
    return color_name in valid_web_colors
if __name__ == '__main__':
    print(is_valid_web_color('red'))
    print(is_valid_web_color('purple'))