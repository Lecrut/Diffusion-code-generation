class FavoriteColors:
    def __init__(self, colors):
        self._colors = tuple(colors)

    def get_colors(self):
        return self._colors

if __name__ == '__main__':
    fav_colors = FavoriteColors(['red', 'blue', 'green'])
    print(fav_colors.get_colors())