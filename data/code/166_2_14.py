class FavoriteColors:

    def __init__(self):
        self.colors = set()

    def add_color(self, color):
        if color not in self.colors:
            self.colors.add(color)

    def has_color(self, color):
        return color in self.colors
if __name__ == '__main__':
    fav_colors = FavoriteColors()
    fav_colors.add_color('red')
    fav_colors.add_color('blue')
    fav_colors.add_color('red')
    print(fav_colors.has_color('red'))
    print(fav_colors.has_color('green'))