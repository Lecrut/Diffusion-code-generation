class WebColorValidator:

    def __init__(self):
        self.valid_colors = {'red', 'green', 'blue', 'yellow', 'black', 'white', 'cyan', 'magenta', 'gray', 'silver', 'gold'}

    def is_valid(self, color_name):
        return color_name in self.valid_colors
if __name__ == '__main__':
    validator = WebColorValidator()
    print(validator.is_valid('red'))
    print(validator.is_valid('purple'))