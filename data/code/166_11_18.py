def is_primary_color(color):
    primary_colors = {'red', 'blue', 'yellow'}
    return color in primary_colors

def filter_primary_colors(color_list):
    return [color for color in color_list if is_primary_color(color)]

if __name__ == '__main__':
    sample_colors = ["red", "blue", "green", "red", "yellow", "purple"]
    filtered_colors = filter_primary_colors(sample_colors)
    print(filtered_colors)