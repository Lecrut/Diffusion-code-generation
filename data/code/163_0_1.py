def print_fruit_color_pairs(fruits, colors):
    for fruit, color in zip(fruits, colors):
        print(f"{fruit}: {color}")
if __name__ == '__main__':
    fruit_list = ["apple", "banana", "cherry", "mango"]
    color_list = ["red", "yellow", "red", "orange"]
    print_fruit_color_pairs(fruit_list, color_list)