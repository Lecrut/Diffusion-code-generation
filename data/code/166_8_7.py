def merge_unique_colors(colors1, colors2):
    unique_colors = set(colors1 + colors2)
    return list(unique_colors)

if __name__ == '__main__':
    sample_colors1 = ["red", "blue", "green"]
    sample_colors2 = ["yellow", "blue", "purple"]
    merged_colors = merge_unique_colors(sample_colors1, sample_colors2)
    print(merged_colors)