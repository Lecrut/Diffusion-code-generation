def filter_primary_colors(colors):
    primary_colors = {'red', 'blue', 'yellow'}
    return [color for color in colors if color.lower() in primary_colors]

if __name__ == '__main__':
    sample_colors = ['red', 'green', 'blue', 'yellow', 'purple']
    print(filter_primary_colors(sample_colors))