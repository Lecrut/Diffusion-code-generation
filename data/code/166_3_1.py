class ColorTracker:
    def __init__(self):
        self.favorite_colors = set()
    def add_color(self, color):
        self.favorite_colors.add(color)
    def display_colors(self):
        print("Tracked Colors:")
        for color in self.favorite_colors:
            print(color)
if __name__ == '__main__':
    tracker = ColorTracker()
    tracker.add_color("Red")
    tracker.add_color("Blue")
    tracker.add_color("Red")
    tracker.add_color("Green")
    tracker.display_colors()