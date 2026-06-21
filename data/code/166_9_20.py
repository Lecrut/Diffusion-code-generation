FAVORITE_COLORS = {'red', 'blue', 'green', 'yellow', 'purple'}

class ColorChecker:

    def __init__(self, colors=FAVORITE_COLORS):
        self.colors = set(colors)

    def has_color(self, color):
        return color in self.colors
if __name__ == '__main__':
    checker = ColorChecker()
    print(checker.has_color('red'))
    print(checker.has_color('orange'))