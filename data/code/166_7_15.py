class ColorFilter:
    @staticmethod
    def filter_colors(colors):
        return [color for color in colors if color.startswith('B')]

if __name__ == '__main__':
    sample_colors = [
        "Red",
        "Blue",
        "green",
        "Brown",
        "black",
        "Beige"
    ]
    filtered_colors = ColorFilter.filter_colors(sample_colors)
    print(filtered_colors)