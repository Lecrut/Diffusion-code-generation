class FavoriteColors:
    def __init__(self):
        self.colors = {}
    def add_color(self, color):
        normalized_color = color.lower()
        if normalized_color in self.colors:
            self.colors[normalized_color] += 1
        else:
            self.colors[normalized_color] = 1
    def get_color_counts(self):
        return self.colors
if __name__ == '__main__':
    fc = FavoriteColors()
    colors_to_add = [
        "Red",
        "blue",
        "red",
        "Green",
        "Blue",
        "purple",
        "red"
    ]
    for color in colors_to_add:
        fc.add_color(color)
    counts = fc.get_color_counts()
    print(counts)