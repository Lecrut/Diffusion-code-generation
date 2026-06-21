favorite_colors = ['red', 'blue', 'green', 'red', 'blue', 'yellow']

def calculate_color_frequency(colors):
    from collections import Counter
    return dict(Counter(colors))

if __name__ == '__main__':
    color_freq = calculate_color_frequency(favorite_colors)
    print(color_freq)