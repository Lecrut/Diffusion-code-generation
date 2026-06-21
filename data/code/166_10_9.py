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
    print("Current colors:", manager.get_colors())
    manager.remove_color("Red")
    print("Colors after removing Red:", manager.get_colors())