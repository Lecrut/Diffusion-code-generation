class FavoriteColors:
    DEFAULT_COLORS = ('red', 'blue', 'green')

    def __init__(self, colors=DEFAULT_COLORS):
        self._colors = tuple(colors)

    def get_colors(self):
        return self._colors

if __name__ == '__main__':
    favorite_colors = FavoriteColors(['purple', 'orange', 'yellow'])
    print(favorite_colors.get_colors())