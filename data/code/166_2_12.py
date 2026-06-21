class FavoriteColors:

    def __init__(self):
        self.colors = set()

    def add_color(self, color):
        if color not in self.colors:
            self.colors.add(color)

    def has_color(self, color):
        return color in self.colors
if __name__ == '__main__':
    favorite_colors = FavoriteColors()
    sample_colors = ['red', 'blue', 'green', 'red', 'blue', 'purple']
    for color in sample_colors:
        favorite_colors.add_color(color)
    print(favorite_colors.has_color('red'))
    print(favorite_colors.has_color('yellow'))