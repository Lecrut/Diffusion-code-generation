class ColorManager:
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
    manager = ColorManager()
    manager.add_color("Red")
    manager.add_color("Blue")
    manager.add_color("Green")
    manager.add_color("Yellow")

    print("Current favorite colors:", manager.get_colors())
    manager.remove_color("Green")
    print("After removing Green:", manager.get_colors())