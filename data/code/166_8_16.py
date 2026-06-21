def merge_unique_colors(colors1, colors2):
    return list(set(colors1 + colors2))

if __name__ == '__main__':
    sample_colors1 = ["red", "blue", "green"]
    sample_colors2 = ["blue", "yellow", "purple"]
    unique_colors = merge_unique_colors(sample_colors1, sample_colors2)
    print(unique_colors)