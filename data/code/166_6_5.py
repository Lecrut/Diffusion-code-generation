class FavoriteColors:
    DEFAULT_COLORS = ('red', 'blue', 'green')

    def __init__(self, colors=DEFAULT_COLORS):
        self._validate_colors(colors)
        self._colors = tuple(colors)

    @staticmethod
    def _validate_colors(colors):
        if not all(isinstance(color, str) for color in colors):
            raise ValueError("All elements must be strings")

    def get_colors(self):
        return self._colors

if __name__ == '__main__':
    favorite_colors = FavoriteColors(['red', 'blue', 'green'])
    print(favorite_colors.get_colors())