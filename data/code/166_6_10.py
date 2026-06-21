class FavoriteColors:
    def __init__(self, colors):
        self._colors = tuple(colors)
    
    def get_colors(self):
        return self._colors

if __name__ == '__main__':
    favorite_colors = FavoriteColors(['pink', 'brown', 'gray'])
    print(favorite_colors.get_colors())