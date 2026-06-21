PRIMARY_COLORS = {"red", "blue", "yellow"}

def filter_primary_colors(color_list):
    return [color for color in color_list if color in PRIMARY_COLORS]

if __name__ == '__main__':
    sample_colors = ["red", "blue", "green", "red", "yellow", "purple"]
    primary_colors = filter_primary_colors(sample_colors)
    print(primary_colors)