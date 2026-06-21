class FavoriteColors:
    def __init__(self):
        self.colors = []

    def add_color(self, color):
        if color not in self.colors:
            self.colors.append(color)

    def remove_color(self, color):
        if color in self.colors:
            self.colors.remove(color)

    def get_colors(self):
        return self.colors

if __name__ == '__main__':
    fc = FavoriteColors()
    fc.add_color('red')
    fc.add_color('blue')
    print(fc.get_colors())
    fc.remove_color('red')
    print(fc.get_colors())