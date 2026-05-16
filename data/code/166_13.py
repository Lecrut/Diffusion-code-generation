class ColorTracker:
    def __init__(self):
        self._favorite_colors = set()
    def add_favorite_color(self, color):
        self._favorite_colors.add(color)
    def display_colors(self):
        return list(self._favorite_colors)
if __name__ == '__main__':
    tracker = ColorTracker()
    tracker.add_favorite_color("Red")
    tracker.add_favorite_color("Blue")
    tracker.add_favorite_color("Green")
    tracker.add_favorite_color("Red")
    print(tracker.display_colors())