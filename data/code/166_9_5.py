def save_colors(filename):
    colors = ["red", "blue", "green", "yellow", "purple"]
    try:
        with open(filename, 'w') as f:
            for color in colors:
                f.write(color + '\n')
    except IOError as e:
        print(f"Error writing to file: {e}")
def load_colors(filename):
    colors = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                colors.append(line.strip())
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty list.")
    except IOError as e:
        print(f"Error reading from file: {e}")
    return colors
if __name__ == '__main__':
    filename = "favorite_colors.txt"
    save_colors(filename)
    loaded_colors = load_colors(filename)
    print("Loaded favorite colors:")
    for color in loaded_colors:
        print(color)