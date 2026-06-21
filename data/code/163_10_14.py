def print_fruit_colors(color_map):
    for fruit, color in color_map.items():
        print(f'{fruit.capitalize()} is {color}.')

if __name__ == '__main__':
    sample_data = {
        'kiwi': 'green',
        'melon': 'yellow',
        'pear': 'green'
    }
    extended_color_map = {
        'apple': 'red',
        'banana': 'yellow',
        'grape': 'purple',
        'orange': 'orange',
        'strawberry': 'red'
    }
    for fruit, color in extended_color_map.items():
        if not isinstance(fruit, str) or not isinstance(color, str):
            raise ValueError("All keys and values must be strings.")
    print_fruit_colors(extended_color_map)