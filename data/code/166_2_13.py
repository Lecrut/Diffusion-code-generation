class FavoriteColors:

    def __init__(self):
        self.colors = set()

    def add_color(self, color):
        if color not in self.colors:
            self.colors.add(color)

    def has_color(self, color):
        return color in self.colors
if __name__ == '__main__':
    favorites = FavoriteColors()
    sample_colors = ['red', 'blue', 'red', 'green', 'blue', 'red', 'done']
    for color in sample_colors:
        if color != 'done':
            favorites.add_color(color)
    print(favorites.colors)