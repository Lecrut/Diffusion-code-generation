primary_colors = {"red", "blue", "yellow"}

def filter_primary_colors(color_list):
    return [color for color in color_list if color in primary_colors]

if __name__ == '__main__':
    sample_colors = ["red", "green", "blue", "purple", "yellow"]
    filtered_colors = filter_primary_colors(sample_colors)
    print(filtered_colors)