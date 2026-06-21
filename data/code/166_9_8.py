class FavoriteColors:

    def __init__(self):
        self.colors = {'red', 'blue', 'green', 'yellow', 'purple'}

    def has_color(self, color):
        return color in self.colors
if __name__ == '__main__':
    favorite_colors = FavoriteColors()
    print(favorite_colors.has_color('red'))
    print(favorite_colors.has_color('black'))