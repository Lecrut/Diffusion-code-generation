class FavoriteColors:
    def __init__(self, colors):
        self._colors = tuple(colors)

if __name__ == '__main__':
    favorite_colors = FavoriteColors(['red', 'blue', 'green'])
    print(favorite_colors._colors)