def validate_color_list(color_list):
    if not isinstance(color_list, list):
        raise ValueError("Input must be a list")
    return color_list

def filter_favorite_colors(color_list):
    validated_colors = validate_color_list(color_list)
    return [color for color in validated_colors if isinstance(color, str)]

if __name__ == '__main__':
    sample_colors = ['red', 'blue', 100, 'green', None, 'yellow']
    valid_colors = filter_favorite_colors(sample_colors)
    print(valid_colors)