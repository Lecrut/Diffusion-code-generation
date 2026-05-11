def save_colors(filename):
    colors = ["red", "blue", "green", "yellow", "purple"]
    with open(filename, "w") as f:
        for color in colors:
            f.write(color + "\n")
def load_colors(filename):
    colors = []
    with open(filename, "r") as f:
        for line in f:
            colors.append(line.strip())
    return colors
if __name__ == '__main__':
    filename = "favorite_colors.txt"
    save_colors(filename)
    loaded_colors = load_colors(filename)
    print("Loaded favorite colors:")
    for color in loaded_colors:
        print(color)