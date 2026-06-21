fruit_colors = {
    'apple': 'red',
    'banana': 'yellow',
    'grape': 'purple',
    'orange': 'orange',
    'strawberry': 'red'
}

def format_fruit_color(fruit, color):
    return f'{fruit.capitalize()} is {color}.'

if __name__ == '__main__':
    formatted_colors = [format_fruit_color(fruit, color) for fruit, color in fruit_colors.items()]
    print('\n'.join(formatted_colors))