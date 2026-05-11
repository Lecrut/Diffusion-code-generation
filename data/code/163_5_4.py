def find_fruit_color_pairs(fruits, colors):
    result = []
    for fruit in fruits:
        first_letter = fruit[0].lower()
        for color in colors:
            if color[0].lower() == first_letter:
                result.append((fruit, color))
    return result
if __name__ == '__main__':
    fruits_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    colors_list = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
    pairs = find_fruit_color_pairs(fruits_list, colors_list)
    print(pairs)