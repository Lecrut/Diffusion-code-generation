def is_valid_color(color):
    return isinstance(color, str)

def filter_favorite_colors(color_list):
    return [color for color in color_list if is_valid_color(color)]

if __name__ == '__main__':
    sample_colors = ['red', 'blue', 100, 'green', None, 'yellow']
    print(filter_favorite_colors(sample_colors))