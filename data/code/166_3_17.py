class ColorCollection:

    def __init__(self):
        self.colors = set()

    def add_color(self, color):
        self.colors.add(color)

    def has_colors(self, *colors_to_check):
        return all((color in self.colors for color in colors_to_check))
if __name__ == '__main__':
    collection = ColorCollection()
    collection.add_color('Red')
    collection.add_color('Blue')
    collection.add_color('Green')
    print(collection.has_colors('Red', 'Blue'))
    print(collection.has_colors('Red', 'Yellow'))