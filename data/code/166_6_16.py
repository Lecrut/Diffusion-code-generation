class FavoriteColors:
    def __init__(self, colors):
        self._validate_colors(colors)
        self._colors = tuple(colors)

    @staticmethod
    def _validate_colors(colors):
        if not all(isinstance(color, str) for color in colors):
            raise ValueError("All elements must be strings")

    def get_colors(self):
        return self._colors

if __name__ == '__main__':
    sample_colors = ['red', 'green', 'blue']
    favorite_colors = FavoriteColors(sample_colors)
    print(favorite_colors.get_colors())