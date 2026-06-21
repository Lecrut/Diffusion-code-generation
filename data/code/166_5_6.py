favorite_colors = ["red", "blue", "green", "yellow", "purple", "orange", "red"]

def calculate_color_frequency(colors):
    frequency = {}
    for color in colors:
        if color in frequency:
            frequency[color] += 1
        else:
            frequency[color] = 1
    return frequency

if __name__ == '__main__':
    color_freq = calculate_color_frequency(favorite_colors)
    print(color_freq)