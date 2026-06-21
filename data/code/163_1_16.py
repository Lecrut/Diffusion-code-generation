def validate_inputs(fruits, colors):
    if not isinstance(fruits, list) or not all(isinstance(fruit, str) for fruit in fruits):
        raise ValueError("Fruits must be a list of strings")
    if not isinstance(colors, list) or not all(isinstance(color, str) for color in colors):
        raise ValueError("Colors must be a list of strings")
    if len(fruits) != len(colors):
        raise ValueError("Fruits and colors lists must have the same length")

def create_fruit_color_pairs(fruits, colors):
    validate_inputs(fruits, colors)
    return list(zip(fruits, colors))

if __name__ == '__main__':
    fruits_list = ["apple", "banana", "cherry"]
    colors_list = ["red", "yellow", "red"]
    pairs = create_fruit_color_pairs(fruits_list, colors_list)
    print(pairs)