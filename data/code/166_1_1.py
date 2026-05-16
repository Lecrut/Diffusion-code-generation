def track_favorite_colors(color_list):
    frequency_map = {}
    for color in color_list:
        if color in frequency_map:
            frequency_map[color] += 1
        else:
            frequency_map[color] = 1
    return frequency_map
if __name__ == '__main__':
    sample_colors = ["red", "blue", "red", "green", "blue", "red", "yellow"]
    result = track_favorite_colors(sample_colors)
    print(result)