class FavoriteColors:

    def __init__(self):
        self.colors = {'red', 'blue', 'green', 'yellow', 'purple'}

    def has_color(self, color):
        return color in self.colors
if __name__ == '__main__':
    fav_colors = FavoriteColors()
    print(fav_colors.has_color('red'))
    print(fav_colors.has_color('black'))