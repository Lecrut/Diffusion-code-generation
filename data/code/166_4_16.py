class FavoriteColorsFilter:
    def __init__(self, colors):
        self.colors = [color for color in colors if isinstance(color, str)]

    def get_valid_colors(self):
        return self.colors

if __name__ == '__main__':
    sample_colors = ['red', 'blue', 100, 'green', None, 'yellow']
    filter_instance = FavoriteColorsFilter(sample_colors)
    print(filter_instance.get_valid_colors())