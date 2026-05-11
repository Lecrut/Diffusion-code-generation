def process_colors(colors):
    color_counts = {}
    for color in colors:
        if color != 'done':
            color_counts[color] = color_counts.get(color, 0) + 1
    return color_counts
if __name__ == '__main__':
    sample_colors = [
        "red",
        "blue",
        "red",
        "green",
        "blue",
        "red",
        "done",
        "green"
    ]
    result = process_colors(sample_colors)
    print(result)