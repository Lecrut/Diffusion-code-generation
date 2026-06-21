class FavoriteColors:
    def __init__(self):
        self.colors = set()

    def add_color(self, color):
        if color not in self.colors:
            self.colors.add(color)

    def get_colors(self):
        return list(self.colors)

if __name__ == '__main__':
    favorite_colors = FavoriteColors()
    colors_to_add = [
        "red",
        "blue",
        "red",
        "green",
        "blue",
        "red"
    ]
    for color in colors_to_add:
        favorite_colors.add_color(color)
    print(favorite_colors.get_colors())