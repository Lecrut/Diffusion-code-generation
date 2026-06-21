def filter_favorite_colors(color_list):
    return [color for color in color_list if isinstance(color, str)]

if __name__ == '__main__':
    sample_colors = ['red', 'blue', 100, 'green', None, 'yellow']
    valid_colors = filter_favorite_colors(sample_colors)
    print(valid_colors)