fruit_color_dict = {
    'apple': 'red',
    'banana': 'yellow'
}

def print_fruit_colors(colors):
    for fruit, color in colors.items():
        print(f"{fruit}: {color}")

if __name__ == '__main__':
    sample_fruits = {
        'grape': 'purple',
        'orange': 'orange',
        'kiwi': 'green'
    }
    print_fruit_colors(sample_fruits)