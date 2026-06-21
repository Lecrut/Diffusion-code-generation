def is_valid_web_color(color_name):
    valid_colors = {'red', 'green', 'blue', 'yellow', 'black', 'white'}
    if color_name in valid_colors:
        return True
    else:
        raise ValueError(f"Invalid web color: {color_name}")

if __name__ == '__main__':
    try:
        print(is_valid_web_color('red'))
    except ValueError as e:
        print(e)

    try:
        print(is_valid_web_color('purple'))
    except ValueError as e:
        print(e)