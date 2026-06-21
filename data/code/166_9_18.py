class FavoriteColors:

    def __init__(self):
        self.colors = set(['red', 'blue', 'green', 'yellow', 'purple'])

    def has_color(self, color):
        return color in self.colors
if __name__ == '__main__':
    fc = FavoriteColors()
    print(fc.has_color('blue'))
    print(fc.has_color('orange'))