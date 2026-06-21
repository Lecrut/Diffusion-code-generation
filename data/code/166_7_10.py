class ColorFilter:
    def __init__(self):
        self.colors = []

    def add_colors(self, color_list):
        self.colors.extend(color_list)

    def filter_colors(self):
        return [color for color in self.colors if color.startswith('B')]

if __name__ == '__main__':
    filter_instance = ColorFilter()
    sample_colors = [
        "Red",
        "blue",
        "red",
        "Blue",
        "green",
        "Black"
    ]
    filter_instance.add_colors(sample_colors)
    filtered_result = filter_instance.filter_colors()
    print(filtered_result)