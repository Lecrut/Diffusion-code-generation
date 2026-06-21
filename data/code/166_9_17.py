class ColorSet:
    def __init__(self):
        self.colors = {"red", "blue", "green", "yellow", "purple"}

    def has_color(self, color):
        return color in self.colors

if __name__ == '__main__':
    colors_set = ColorSet()
    sample_colors = ["red", "orange", "green"]
    for color in sample_colors:
        print(f"Checking if {color} is a favorite color: {colors_set.has_color(color)}")