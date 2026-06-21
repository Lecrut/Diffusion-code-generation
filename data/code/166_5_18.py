class FavoriteColors:
    def __init__(self):
        self.colors = ["red", "blue", "green", "yellow", "purple", "orange"]

    def get_frequency(self):
        from collections import Counter
        color_counts = Counter(self.colors)
        return dict(color_counts)

if __name__ == '__main__':
    fc = FavoriteColors()
    frequency = fc.get_frequency()
    print(frequency)