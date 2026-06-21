class FavoriteColors:
    COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]

    @staticmethod
    def count_frequencies(colors):
        frequency = {}
        for color in colors:
            if color in frequency:
                frequency[color] += 1
            else:
                frequency[color] = 1
        return frequency

if __name__ == '__main__':
    sample_colors = ["red", "blue", "green", "yellow", "purple", "orange", "red"]
    frequencies = FavoriteColors.count_frequencies(sample_colors)
    print(frequencies)