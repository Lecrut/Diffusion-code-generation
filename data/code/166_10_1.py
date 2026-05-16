class ColorManager:
    def __init__(self):
        self.favorite_colors = {}
    def add_favorite_color(self, color):
        self.favorite_colors[color] = True
    def display_colors(self):
        for color, exists in self.favorite_colors.items():
            if exists:
                print(f"Favorite color: {color}")
if __name__ == '__main__':
    manager = ColorManager()
    manager.add_favorite_color("Red")
    manager.add_favorite_color("Blue")
    manager.add_favorite_color("Green")
    manager.add_favorite_color("Yellow")
    manager.display_colors()