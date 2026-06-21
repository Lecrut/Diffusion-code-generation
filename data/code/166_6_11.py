class FavoriteColors:
    def __init__(self, colors):
        if not all(isinstance(color, str) for color in colors):
            raise ValueError("All elements must be strings")
        self._colors = tuple(colors)

    def get_colors(self):
        return self._colors

if __name__ == '__main__':
    favorite_colors = FavoriteColors(['red', 'blue', 'green'])
    print(favorite_colors.get_colors())