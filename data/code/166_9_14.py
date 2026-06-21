class FavoriteColors:
    DEFAULT_COLORS = {'red', 'blue', 'green', 'yellow', 'purple'}

    def __init__(self):
        self.colors = self.DEFAULT_COLORS

    def has_color(self, color):
        return color in self.colors
if __name__ == '__main__':
    fc = FavoriteColors()
    print(fc.has_color('red'))
    print(fc.has_color('black'))