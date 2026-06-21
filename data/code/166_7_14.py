def filter_colors(colors):
    return [color for color in colors if color.startswith('B')]

if __name__ == '__main__':
    sample_colors = [
        "Blue",
        "green",
        "Brown",
        "black",
        "blue"
    ]
    filtered_colors = filter_colors(sample_colors)
    print(filtered_colors)