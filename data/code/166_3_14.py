class ColorTracker:
    def __init__(self):
        self.colors = set()

    def add_color(self, color):
        self.colors.add(color)

    def check_colors(self, *colors_to_check):
        return all(color in self.colors for color in colors_to_check)

if __name__ == '__main__':
    tracker = ColorTracker()
    tracker.add_color("Red")
    tracker.add_color("Blue")
    tracker.add_color("Green")

    print(tracker.check_colors("Red", "Blue"))
    print(tracker.check_colors("Yellow"))