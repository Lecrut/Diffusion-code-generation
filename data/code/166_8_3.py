import collections
def find_top_5_colors(color_list):
    color_counts = collections.Counter(color_list)
    sorted_colors = color_counts.most_common(5)
    return sorted_colors
if __name__ == '__main__':
    sample_colors = [
        "red", "blue", "green", "red", "blue", "red", "yellow", "blue",
        "green", "red", "purple", "blue", "red", "orange", "yellow",
        "red", "blue", "green", "red", "purple", "blue", "red", "yellow",
        "pink", "cyan", "magenta", "red", "blue"
    ]
    top_colors = find_top_5_colors(sample_colors)
    print(top_colors)