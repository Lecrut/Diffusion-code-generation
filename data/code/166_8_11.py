def merge_favorite_colors(colors1, colors2):
    return list(dict.fromkeys(colors1 + colors2))

if __name__ == '__main__':
    sample_colors_1 = ["red", "blue", "green"]
    sample_colors_2 = ["green", "yellow", "blue"]
    merged_colors = merge_favorite_colors(sample_colors_1, sample_colors_2)
    print(merged_colors)