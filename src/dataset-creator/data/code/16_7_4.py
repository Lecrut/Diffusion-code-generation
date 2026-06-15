def create_color_map():
    color_to_name = {
        "red": "Red",
        "green": "Green",
        "blue": "Blue",
        "yellow": "Yellow",
        "purple": "Purple",
        "orange": "Orange",
        "cyan": "Cyan",
        "magenta": "Magenta"
    }
    return color_to_name
if __name__ == '__main__':
    color_map = create_color_map()
    test_colors = ["red", "green", "blue", "yellow", "purple", "orange", "cyan", "magenta"]
    print("Color to Name Mapping:")
    for color in test_colors:
        if color in color_map:
            name = color_map[color]
            print(f"{color}: {name}")
        else:
            print(f"{color}: Not Found")