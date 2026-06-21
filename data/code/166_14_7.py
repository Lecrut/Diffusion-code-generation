VALID_COLORS = {'red', 'green', 'blue', 'yellow', 'black', 'white', 'cyan', 'magenta', 'gray', 'silver', 'gold'}

def is_valid_web_color(color_name):
    return color_name in VALID_COLORS
if __name__ == '__main__':
    print(is_valid_web_color('red'))
    print(is_valid_web_color('purple'))