def save_colors(filename):
    colors = ["red", "blue", "green", "yellow", "purple"]
    try:
        with open(filename, 'w') as f:
            for color in colors:
                f.write(color + '\n')
    except IOError:
        pass
def load_colors(filename):
    colors = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                colors.append(line.strip())
    except IOError:
        pass
    return colors
if __name__ == '__main__':
    filename = "favorite_colors.txt"
    save_colors(filename)
    loaded_colors = load_colors(filename)
    print("Loaded favorite colors:")
    for color in loaded_colors:
        print(color)