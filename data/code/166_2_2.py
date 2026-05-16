def process_colors(sample_colors):
    color_counts = {}
    for color in sample_colors:
        if color != 'done':
            if color in color_counts:
                color_counts[color] += 1
            else:
                color_counts[color] = 1
    return color_counts
if __name__ == '__main__':
    sample_input = [
        "red",
        "blue",
        "red",
        "green",
        "blue",
        "red",
        "done",
        "green"
    ]
    results = process_colors(sample_input)
    for color, count in results.items():
        print(f"{color}: {count}")