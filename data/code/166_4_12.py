FILTERED_COLOR_LIST = []

def filter_favorite_colors(color_list):
    global FILTERED_COLOR_LIST
    FILTERED_COLOR_LIST = [color for color in color_list if isinstance(color, str)]
    return FILTERED_COLOR_LIST

if __name__ == '__main__':
    sample_colors = ['red', 'blue', 100, 'green', None, 'yellow']
    filtered_colors = filter_favorite_colors(sample_colors)
    print(filtered_colors)