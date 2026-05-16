def create_fruit_color_map(fruits, colors):
    fruit_color_map = {}
    for i in range(len(fruits)):
        fruit_color_map[fruits[i]] = colors[i]
    return fruit_color_map
if __name__ == '__main__':
    fruits_list = ["apple", "banana", "cherry", "date"]
    colors_list = ["red", "yellow", "red", "brown"]
    color_map = create_fruit_color_map(fruits_list, colors_list)
    print(color_map)