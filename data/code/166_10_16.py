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

    print("Current favorite colors:")
    for color in manager.get_colors():
        print(f"Favorite color: {color}")

    manager.remove_color("Blue")
    print("\nAfter removing Blue:")
    for color in manager.get_colors():
        print(f"Favorite color: {color}")