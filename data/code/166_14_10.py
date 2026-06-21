class WebColorValidator:
    VALID_COLORS = {'red', 'green', 'blue', 'yellow', 'black', 'white', 'cyan', 'magenta', 'gray', 'silver', 'gold'}

    @staticmethod
    def is_valid_web_color(color_name):
        return color_name in WebColorValidator.VALID_COLORS

if __name__ == '__main__':
    print(WebColorValidator.is_valid_web_color('red'))
    print(WebColorValidator.is_valid_web_color('purple'))