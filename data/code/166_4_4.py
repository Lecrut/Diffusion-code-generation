def filter_favorite_colors(colors):
    return [color for color in colors if isinstance(color, str)]

if __name__ == '__main__':
    sample_colors = ['red', 'blue', 42, 'green', None, 'yellow']
    filtered_colors = filter_favorite_colors(sample_colors)
    print(filtered_colors)