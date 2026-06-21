fruit_colors = {
    'apple': 'red',
    'banana': 'yellow',
    'grape': 'purple',
    'orange': 'orange',
    'strawberry': 'red'
}

def format_and_print_fruit_colors(color_map):
    for fruit, color in color_map.items():
        print(f'{fruit.capitalize()} is {color}.')

if __name__ == '__main__':
    format_and_print_fruit_colors(fruit_colors)