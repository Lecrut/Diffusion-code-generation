def save_colors(filename):
    colors = ["red", "blue", "green", "yellow", "purple"]
    try:
        with open(filename, 'w') as f:
            for color in colors:
                f.write(color + '\n')
        print(f"Colors saved to {filename}")
    except IOError as e:
        print(f"Error saving file: {e}")
def load_colors(filename):
    loaded_colors = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                loaded_colors.append(line.strip())
        print(f"Colors loaded from {filename}")
        return loaded_colors
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with default colors.")
        return ["red", "blue", "green", "yellow", "purple"]
    except IOError as e:
        print(f"Error loading file: {e}")
        return []
if __name__ == '__main__':
    file_name = "favorite_colors.txt"
    save_colors(file_name)
    loaded = load_colors(file_name)
    print("Loaded favorite colors:")
    for color in loaded:
        print(color)