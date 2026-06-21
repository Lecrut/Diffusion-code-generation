def initialize_favorite_colors():
    colors = ["red", "blue", "green", "yellow", "purple"]
    return sorted(colors)

if __name__ == '__main__':
    sample_colors = initialize_favorite_colors()
    print(sample_colors)