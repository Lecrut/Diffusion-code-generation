def validate_fruit_list(fruit_list):
    if not all(isinstance(fruit, str) for fruit in fruit_list):
        raise ValueError("All elements in the input list must be strings.")

def pair_fruits_with_colors(fruit_list):
    fruit_colors = {
        'apple': 'red',
        'banana': 'yellow',
        'grape': 'purple',
        'orange': 'orange',
        'strawberry': 'red',
        'lemon': 'yellow'
    }
    validate_fruit_list(fruit_list)
    return [(fruit, fruit_colors.get(fruit, 'unknown')) for fruit in fruit_list]

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'grape', 'orange', 'strawberry', 'lemon']
    print(pair_fruits_with_colors(fruits))