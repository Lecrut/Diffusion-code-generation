def map_color_to_name(color_map, color_code):
    return color_map.get(color_code)
if __name__ == '__main__':
    color_dictionary = {
        "red": "Red",
        "green": "Green",
        "blue": "Blue",
        "yellow": "Yellow",
        "cyan": "Cyan"
    }
    test_code_1 = "red"
    result_1 = map_color_to_name(color_dictionary, test_code_1)
    print(f"{test_code_1}: {result_1}")
    test_code_2 = "blue"
    result_2 = map_color_to_name(color_dictionary, test_code_2)
    print(f"{test_code_2}: {result_2}")
    test_code_3 = "magenta"
    result_3 = map_color_to_name(color_dictionary, test_code_3)
    print(f"{test_code_3}: {result_3}")