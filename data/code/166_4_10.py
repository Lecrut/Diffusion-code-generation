def filter_favorite_colors(colors):
    return [color for color in colors if isinstance(color, str)]

if __name__ == '__main__':
    sample_colors = ['red', 'blue', 3, 'green', None, 'yellow']
    print(filter_favorite_colors(sample_colors))