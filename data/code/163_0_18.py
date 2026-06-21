fruit_color_map = {
    'apple': 'red',
    'banana': 'yellow'
}

def validate_fruit_colors(fruits):
    if not fruits:
        raise ValueError("Fruit list cannot be empty")
    for fruit in fruits:
        if fruit not in fruit_color_map:
            raise KeyError(f"Unknown fruit: {fruit}")

if __name__ == '__main__':
    sample_fruits = ['apple', 'banana']
    validate_fruit_colors(sample_fruits)
    for fruit in sample_fruits:
        print(f"{fruit}: {fruit_color_map[fruit]}")