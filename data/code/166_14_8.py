def is_valid_web_color(color_name):
    valid_colors = {'red', 'green', 'blue', 'yellow', 'black', 'white', 'cyan', 'magenta', 'yellow', 'gray', 'silver', 'gold'}
    return color_name.lower() in valid_colors
if __name__ == '__main__':
    print(is_valid_web_color('Red'))
    print(is_valid_web_color('purple'))