def map_color_to_name(color_map, color_code):
    return color_map.get(color_code)
if __name__ == '__main__':
    color_data = {
        "red": "Red",
        "green": "Green",
        "blue": "Blue",
        "yellow": "Yellow",
        "cyan": "Cyan"
    }
    code1 = "red"
    name1 = map_color_to_name(color_data, code1)
    print(f"{code1}: {name1}")
    code2 = "blue"
    name2 = map_color_to_name(color_data, code2)
    print(f"{code2}: {name2}")
    code3 = "magenta"
    name3 = map_color_to_name(color_data, code3)
    print(f"{code3}: {name3}")