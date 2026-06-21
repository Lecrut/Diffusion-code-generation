class FavoriteColors:
    def __init__(self):
        self.colors = set()

    def add_color(self, color):
        if color not in self.colors:
            self.colors.add(color)

    def get_colors(self):
        return list(self.colors)

if __name__ == '__main__':
    favorite_colors_manager = FavoriteColors()
    sample_colors = [
        "red",
        "blue",
        "red",
        "green",
        "blue",
        "red",
    ]
    for color in sample_colors:
        favorite_colors_manager.add_color(color)
    
    print(favorite_colors_manager.get_colors())