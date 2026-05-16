def save_colors(filename):
    colors = ["red", "blue", "green", "yellow", "purple"]
    try:
        with open(filename, 'w') as f:
            for color in colors:
                f.write(color + '\n')
        print(f"Colors saved to {filename}")
    except IOError:
        print(f"Error: Could not write to file {filename}")
def load_colors(filename):
    loaded_colors = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                loaded_colors.append(line.strip())
        print(f"Colors loaded from {filename}: {loaded_colors}")
        return loaded_colors
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with default colors.")
        return ["red", "blue", "green", "yellow", "purple"]
    except IOError:
        print(f"Error: Could not read from file {filename}")
        return []
if __name__ == '__main__':
    filename = "favorite_colors.txt"
    save_colors(filename)
    loaded = load_colors(filename)