FRUIT_COLOR_MAP = {
    'apple': 'red',
    'banana': 'yellow',
    'grape': 'purple',
    'orange': 'orange',
    'strawberry': 'red',
    'lemon': 'yellow'
}

def pair_fruits_with_colors(fruit_list):
    return [(fruit, FRUIT_COLOR_MAP.get(fruit, 'unknown')) for fruit in fruit_list]

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'grape', 'orange', 'strawberry', 'lemon']
    print(pair_fruits_with_colors(fruits))