from collections import Counter

class ColorFrequencyCounter:
    def __init__(self):
        self._colors = []

    def add_color(self, color):
        self._colors.append(color)

    def get_frequency(self):
        color_count = Counter(self._colors)
        return sorted(color_count.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    counter = ColorFrequencyCounter()
    counter.add_color("Red")
    counter.add_color("Blue")
    counter.add_color("Green")
    counter.add_color("Red")
    print(counter.get_frequency())