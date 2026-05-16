class ColorManager:
    def __init__(self):
        self.favorite_colors = {}
    def add_color(self, color):
        self.favorite_colors[color] = True
    def display_colors(self):
        for color, exists in self.favorite_colors.items():
            if exists:
                print(f"Favorite color: {color}")
if __name__ == '__main__':
    manager = ColorManager()
    manager.add_color("Red")
    manager.add_color("Blue")
    manager.add_color("Green")
    manager.add_color("Yellow")
    manager.display_colors()