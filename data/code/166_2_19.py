class FavoriteColors:

    def __init__(self):
        self.colors = set()

    def add_color(self, color):
        if color is not None:
            self.colors.add(color)

    def get_colors(self):
        return list(self.colors)
if __name__ == '__main__':
    favorite_colors = FavoriteColors()
    favorite_colors.add_color('red')
    favorite_colors.add_color('blue')
    favorite_colors.add_color('red')
    favorite_colors.add_color(None)
    print(favorite_colors.get_colors())