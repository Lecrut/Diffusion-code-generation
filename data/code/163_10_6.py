FRUIT_COLORS = {
    'apple': 'red',
    'banana': 'yellow',
    'grape': 'purple',
    'orange': 'orange',
    'strawberry': 'red'
}

def print_fruit_colors(color_map):
    for fruit, color in color_map.items():
        print(f'{fruit.capitalize()} is {color}.')

if __name__ == '__main__':
    print_fruit_colors(FRUIT_COLORS)