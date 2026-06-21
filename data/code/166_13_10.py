from collections import Counter

class ColorFrequencyCounter:
    def __init__(self):
        self._favorite_colors = ["red", "blue", "green", "red", "blue", "red"]

    @staticmethod
    def count_frequency(colors):
        return sorted(Counter(colors).items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    counter = ColorFrequencyCounter()
    result = counter.count_frequency(counter._favorite_colors)
    print(result)