favorite_colors = ['red', 'blue', 'green', 'blue', 'red', 'yellow']

def calculate_color_frequency(colors):
    color_count = {}
    for color in colors:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    return color_count

if __name__ == '__main__':
    frequency = calculate_color_frequency(favorite_colors)
    print(frequency)