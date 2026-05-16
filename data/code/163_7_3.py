def fruit_colors_generator(fruits, colors):
    for fruit, color in zip(fruits, colors):
        yield (fruit, color)
if __name__ == '__main__':
    fruits_list = ["apple", "banana", "cherry", "date"]
    colors_list = ["red", "yellow", "red", "brown"]
    fruit_color_gen = fruit_colors_generator(fruits_list, colors_list)
    results = list(fruit_color_gen)
    print(results)