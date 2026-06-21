def map_fruit_colors(fruit_color_pairs):
    return {fruit: color for fruit, color in fruit_color_pairs}

def pair_fruits_with_standard_colors(fruits):
    standard_colors = {
        'apple': 'red',
        'banana': 'yellow',
        'grape': 'purple',
        'orange': 'orange',
        'strawberry': 'red',
        'lemon': 'yellow'
    }
    return [(fruit, standard_colors.get(fruit, 'unknown')) for fruit in fruits]

if __name__ == '__main__':
    sample_fruits = ['apple', 'banana', 'grape', 'orange', 'strawberry', 'kiwi']
    color_map = map_fruit_colors([
        ("apple", "red"),
        ("banana", "yellow"),
        ("grape", "purple"),
        ("orange", "orange"),
        ("strawberry", "red"),
        ("lemon", "yellow")
    ])
    paired_fruits = pair_fruits_with_standard_colors(sample_fruits)
    print(paired_fruits)