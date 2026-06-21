def map_fruit_colors(fruit_color_pairs):
    return {fruit: color for fruit, color in fruit_color_pairs}

def pair_fruits_with_colors(fruit_list, color_map):
    return [(fruit, color_map.get(fruit, 'unknown')) for fruit in fruit_list]

if __name__ == '__main__':
    fruit_color_data = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("grape", "purple"),
        ("orange", "orange"),
        ("strawberry", "red"),
        ("lemon", "yellow")
    ]
    
    color_map = map_fruit_colors(fruit_color_data)
    fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
    paired_fruits = pair_fruits_with_colors(fruits, color_map)
    print(paired_fruits)