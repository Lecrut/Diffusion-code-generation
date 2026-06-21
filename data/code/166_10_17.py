class ColorManager:
    def __init__(self):
        self.favorite_colors = []

    def add_color(self, color):
        if color not in self.favorite_colors:
            self.favorite_colors.append(color)

    def remove_color(self, color):
        if color in self.favorite_colors:
            self.favorite_colors.remove(color)

    def get_colors(self):
        return self.favorite_colors

if __name__ == '__main__':
    manager = ColorManager()
    manager.add_color("Red")
    manager.add_color("Blue")
    manager.add_color("Green")
    manager.add_color("Yellow")

    print("Current favorite colors:", manager.get_colors())

    manager.remove_color("Blue")
    print("After removing Blue:", manager.get_colors())