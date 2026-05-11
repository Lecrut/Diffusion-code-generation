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
    manager = FavoriteColors()
    colors_to_add = [
        "Red",
        "blue",
        "red",
        "Green",
        "Blue",
        "purple"
    ]
    for color in colors_to_add:
        manager.add_color(color)
    counts = manager.get_color_counts()
    print(counts)