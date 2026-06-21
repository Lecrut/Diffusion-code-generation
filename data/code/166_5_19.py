favorite_colors = ['red', 'blue', 'green', 'red', 'blue', 'yellow']

color_frequency = {}
for color in favorite_colors:
    if color in color_frequency:
        color_frequency[color] += 1
    else:
        color_frequency[color] = 1

if __name__ == '__main__':
    print(color_frequency)