def create_fruit_color_dict():
    fruit_colors = {
        'apple': 'red',
        'banana': 'yellow'
    }
    return fruit_colors

def print_fruit_colors(fruits, colors):
    for fruit, color in zip(fruits, colors):
        print(f"{fruit}: {color}")

if __name__ == '__main__':
    fruits = ["apple", "banana"]
    colors = ["red", "yellow"]
    
    if len(fruits) != len(colors):
        raise ValueError("Fruit and color lists must have the same number of elements.")
    
    fruit_color_dict = create_fruit_color_dict()
    print_fruit_colors(fruits, colors)