def validate_inputs(fruits, colors):
    if not isinstance(fruits, list) or not all(isinstance(fruit, str) for fruit in fruits):
        raise ValueError("Fruits must be a list of strings")
    if not isinstance(colors, list) or not all(isinstance(color, str) for color in colors):
        raise ValueError("Colors must be a list of strings")
    if len(fruits) != len(colors):
        raise ValueError("Fruits and colors lists must have the same length")

def create_fruit_color_dict(fruits, colors):
    validate_inputs(fruits, colors)
    return {fruit: color for fruit, color in zip(fruits, colors)}

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'green']
    fruit_color_dict = create_fruit_color_dict(fruits, colors)
    print(fruit_color_dict)