def initialize_favorite_colors():
    colors = ["red", "blue", "green", "yellow", "purple"]
    return sorted(colors)

if __name__ == '__main__':
    favorite_colors = initialize_favorite_colors()
    print(favorite_colors)