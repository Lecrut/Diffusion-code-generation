favorite_colors = {
    "red": 0,
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "purple": 0,
    "orange": 0
}

def count_frequencies(colors):
    for color in colors:
        if color in favorite_colors:
            favorite_colors[color] += 1

if __name__ == '__main__':
    sample_colors = ["red", "blue", "green", "yellow", "purple", "orange", "red"]
    count_frequencies(sample_colors)
    print(favorite_colors)