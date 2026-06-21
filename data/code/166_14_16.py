def is_valid_web_color(color_name):
    valid_colors = {'red', 'green', 'blue', 'yellow', 'black', 'white'}
    return color_name.lower() in valid_colors

if __name__ == '__main__':
    test_colors = ['Red', 'purple', 'GREEN', 'blue']
    for color in test_colors:
        print(f"{color}: {is_valid_web_color(color)}")