if __name__ == '__main__':
    color_to_name_map = {
        "red": "Red",
        "green": "Green",
        "blue": "Blue",
        "yellow": "Yellow",
        "purple": "Purple",
        "orange": "Orange",
        "cyan": "Cyan",
        "magenta": "Magenta"
    }
    input_color = "red"
    if input_color in color_to_name_map:
        result_name = color_to_name_map[input_color]
        print(f"The name for {input_color} is {result_name}")
    else:
        print(f"{input_color} not found in the map.")