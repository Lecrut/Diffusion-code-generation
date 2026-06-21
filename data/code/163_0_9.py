fruit_color_mapping = {
    'apple': 'red',
    'banana': 'yellow'
}

def display_fruit_colors(mapping):
    for fruit, color in mapping.items():
        print(f"{fruit}: {color}")

if __name__ == '__main__':
    sample_fruits = ['apple', 'banana']
    sample_colors = ['red', 'yellow']
    fruit_color_dict = dict(zip(sample_fruits, sample_colors))
    display_fruit_colors(fruit_color_dict)