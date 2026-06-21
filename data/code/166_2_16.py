class FavoriteColors:

    def __init__(self):
        self.colors = set()

    def add_color(self, color):
        if color not in self.colors:
            self.colors.add(color)

    def get_colors(self):
        return list(self.colors)
if __name__ == '__main__':
    fav_colors = FavoriteColors()
    fav_colors.add_color('red')
    fav_colors.add_color('blue')
    fav_colors.add_color('green')
    fav_colors.add_color('red')
    print(fav_colors.get_colors())