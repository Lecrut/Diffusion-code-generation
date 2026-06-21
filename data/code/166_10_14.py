class ColorManager:
    DEFAULT_COLORS = ["Red", "Blue", "Green", "Yellow"]

    def __init__(self):
        self.favorite_colors = {}

    def add_color(self, color):
        self.favorite_colors[color] = True

    def remove_color(self, color):
        if color in self.favorite_colors:
            del self.favorite_colors[color]

    def get_favorite_colors(self):
        return list(self.favorite_colors.keys())

if __name__ == '__main__':
    manager = ColorManager()
    for color in ColorManager.DEFAULT_COLORS:
        manager.add_color(color)
    print("Current favorite colors:", manager.get_favorite_colors())
    manager.remove_color("Green")
    print("After removing Green:", manager.get_favorite_colors())