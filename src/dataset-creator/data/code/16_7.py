def create_color_to_name_map():
    color_map = {
        "red": "crimson",
        "blue": "azure",
        "green": "emerald",
        "yellow": "gold",
        "purple": "violet",
        "orange": "tangerine"
    }
    return color_map
if __name__ == '__main__':
    color_names = create_color_to_name_map()
    test_colors = ["red", "blue", "green", "yellow", "purple", "orange", "black"]
    print("Color to Name Mapping Results:")
    for color in test_colors:
        if color in color_names:
            print(f"{color}: {color_names[color]}")
        else:
            print(f"{color}: Not found")