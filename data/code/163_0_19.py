fruit_color_map = {
    'apple': 'red',
    'banana': 'yellow'
}

def print_fruit_colors(fruit_color_dict):
    for fruit, color in fruit_color_dict.items():
        print(f"{fruit}: {color}")

if __name__ == '__main__':
    print_fruit_colors(fruit_color_map)