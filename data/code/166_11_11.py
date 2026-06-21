def filter_primary_colors(color_list):
    primary_colors = {'red', 'blue', 'yellow'}
    return [color for color in color_list if color in primary_colors]

if __name__ == '__main__':
    sample_colors = ["red", "blue", "green", "red", "yellow", "purple"]
    result = filter_primary_colors(sample_colors)
    print(result)