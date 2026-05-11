def find_fruit_color_pairs(fruits, colors):
    fruit_color_pairs = []
    for fruit in fruits:
        for color in colors:
            if fruit[0].lower() == color[0].lower():
                fruit_color_pairs.append((fruit, color))
    return fruit_color_pairs
if __name__ == '__main__':
    fruits_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    colors_list = ["Red", "Blue", "Green", "Yellow", "Purple"]
    result = find_fruit_color_pairs(fruits_list, colors_list)
    print(result)