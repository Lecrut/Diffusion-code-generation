def count_favorite_colors(colors):
    color_count = {}
    for color in colors:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    return color_count

if __name__ == '__main__':
    sample_colors = ["red", "blue", "green", "yellow", "purple", "orange", "red"]
    validated_colors = [color for color in sample_colors if isinstance(color, str)]
    frequency_dict = count_favorite_colors(validated_colors)
    print(frequency_dict)