if __name__ == '__main__':
    color_to_name = {
        "red": "Red",
        "green": "Green",
        "blue": "Blue",
        "yellow": "Yellow",
        "purple": "Purple",
        "orange": "Orange"
    }
    input_colors = ["red", "blue", "yellow", "green", "purple", "orange", "cyan"]
    result_names = []
    for color in input_colors:
        if color in color_to_name:
            result_names.append(color_to_name[color])
        else:
            result_names.append(f"Unknown: {color}")
    print(result_names)