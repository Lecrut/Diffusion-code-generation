def process_colors(color_list):
    color_counts = {}
    for color in color_list:
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
    return color_counts
if __name__ == '__main__':
    sample_colors = [
        "red",
        "blue",
        "red",
        "green",
        "blue",
        "red",
        "yellow",
        "green",
        "blue",
        "red",
        "purple"
    ]
    counts = process_colors(sample_colors)
    for color, count in counts.items():
        print(f"{color}: {count}")