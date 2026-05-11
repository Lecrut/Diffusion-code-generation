def find_fruit_color_pairs(fruits, colors):
    result = []
    for fruit in fruits:
        for color in colors:
            if fruit[0].lower() == color[0].lower():
                result.append((fruit, color))
    return result
if __name__ == '__main__':
    fruits_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    colors_list = ["Red", "Green", "Blue", "Yellow", "Purple"]
    pairs = find_fruit_color_pairs(fruits_list, colors_list)
    print(pairs)