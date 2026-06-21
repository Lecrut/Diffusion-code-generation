fruit_colors = {
    'apple': 'red',
    'banana': 'yellow',
    'grape': 'purple',
    'orange': 'orange',
    'strawberry': 'red'
}

def print_fruit_colors(color_map):
    if not isinstance(color_map, dict):
        raise ValueError("Input must be a dictionary.")
    
    for fruit, color in color_map.items():
        if not isinstance(fruit, str) or not isinstance(color, str):
            raise ValueError("Dictionary keys and values must be strings.")
        
        print(f'{fruit.capitalize()} is {color}.')

if __name__ == '__main__':
    try:
        print_fruit_colors(fruit_colors)
    except ValueError as e:
        print(e)