class ColorManager:
    def __init__(self):
        self._favorite_colors = []

    @staticmethod
    def _is_valid_color(color):
        valid_colors = ["Red", "Blue", "Green", "Yellow"]
        return color in valid_colors

    def add_color(self, color):
        if self._is_valid_color(color) and color not in self._favorite_colors:
            self._favorite_colors.append(color)

    def remove_color(self, color):
        if color in self._favorite_colors:
            self._favorite_colors.remove(color)

    def get_favorite_colors(self):
        return self._favorite_colors

if __name__ == '__main__':
    manager = ColorManager()
    manager.add_color("Red")
    manager.add_color("Blue")
    manager.add_color("Green")
    manager.add_color("Yellow")
    print("Favorite Colors:", manager.get_favorite_colors())
    manager.remove_color("Blue")
    print("Updated Favorite Colors:", manager.get_favorite_colors())