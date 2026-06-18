if __name__ == '__main__':
    color_to_name = {
        "red": "Red",
        "green": "Green",
        "blue": "Blue",
        "yellow": "Yellow",
        "purple": "Purple",
        "orange": "Orange"
    }
    input_colors = ["red", "green", "blue", "yellow", "purple", "orange", "cyan"]
    color_names = {}
    for color in input_colors:
        if color in color_to_name:
            color_names[color] = color_to_name[color]
        else:
            color_names[color] = "Color Not Found"
    print(color_names)