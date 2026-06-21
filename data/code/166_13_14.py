class ColorFrequency:
    def __init__(self):
        self._color_count = {}

    def add_color(self, color):
        if color in self._color_count:
            self._color_count[color] += 1
        else:
            self._color_count[color] = 1

    def get_sorted_colors(self):
        return sorted(self._color_count.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    tracker = ColorFrequency()
    tracker.add_color("Red")
    tracker.add_color("Blue")
    tracker.add_color("Green")
    tracker.add_color("Red")
    print(tracker.get_sorted_colors())