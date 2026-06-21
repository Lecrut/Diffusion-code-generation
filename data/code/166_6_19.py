class FavoriteColors:
    def __init__(self, colors):
        self._colors = tuple(colors)
    
    def get_colors(self):
        return self._colors

if __name__ == '__main__':
    sample_colors = ['pink', 'cyan', 'lime']
    favorite_colors_instance = FavoriteColors(sample_colors)
    print(favorite_colors_instance.get_colors())