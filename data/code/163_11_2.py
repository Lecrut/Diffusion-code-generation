def pair_fruits_with_colors(fruit_list):
    fruit_colors = {
        'apple': 'red',
        'banana': 'yellow',
        'grape': 'purple',
        'orange': 'orange',
        'strawberry': 'red',
        'lemon': 'yellow'
    }
    return [(fruit, fruit_colors.get(fruit, 'unknown')) for fruit in fruit_list]

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'grape', 'orange', 'strawberry', 'lemon']
    print(pair_fruits_with_colors(fruits))