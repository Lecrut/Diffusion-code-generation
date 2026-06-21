class FavoriteColors:

    def __init__(self):
        self.colors = {'red', 'blue', 'green', 'yellow', 'purple'}

    def contains_color(self, color):
        return color in self.colors
if __name__ == '__main__':
    colors = FavoriteColors()
    print(colors.contains_color('red'))
    print(colors.contains_color('orange'))