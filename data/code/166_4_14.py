class ColorFilter:
    @staticmethod
    def is_valid_color(color):
        return isinstance(color, str)

    @classmethod
    def filter_favorite_colors(cls, color_list):
        return [color for color in color_list if cls.is_valid_color(color)]

if __name__ == '__main__':
    sample_colors = ['red', 'blue', 100, 'green', None, 'yellow']
    filtered_colors = ColorFilter.filter_favorite_colors(sample_colors)
    print(filtered_colors)