def fruit_colors_generator(fruits, colors):
    for fruit, color in zip(fruits, colors):
        yield (fruit, color)
if __name__ == '__main__':
    fruits_list = ["apple", "banana", "cherry", "date"]
    colors_list = ["red", "yellow", "red", "brown"]
    color_pairs = fruit_colors_generator(fruits_list, colors_list)
    for fruit, color in color_pairs:
        print(f"{fruit}: {color}")