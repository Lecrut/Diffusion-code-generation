COLOR_PREFIX = 'B'

def filter_colors(colors):
    return [color for color in colors if color.startswith(COLOR_PREFIX)]

if __name__ == '__main__':
    sample_colors = [
        "Red",
        "Blue",
        "green",
        "Brown",
        "black"
    ]
    filtered_colors = filter_colors(sample_colors)
    print(filtered_colors)