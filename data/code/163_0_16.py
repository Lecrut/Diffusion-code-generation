fruit_color_map = {
    'apple': 'red',
    'banana': 'yellow'
}

def print_fruit_colors(fruits):
    for fruit, color in fruits.items():
        print(f"{fruit}: {color}")

if __name__ == '__main__':
    sample_fruit_colors = {'grape': 'purple', 'kiwi': 'green'}
    print_fruit_colors(sample_fruit_colors)