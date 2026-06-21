def create_fruit_color_dict(fruits, colors):
    if not isinstance(fruits, list) or not all(isinstance(fruit, str) for fruit in fruits):
        raise ValueError("Fruits must be a list of strings")
    if not isinstance(colors, list) or not all(isinstance(color, str) for color in colors):
        raise ValueError("Colors must be a list of strings")
    if len(fruits) != len(colors):
        raise ValueError("Fruits and colors lists must have the same length")

    return {fruit: color for fruit, color in zip(fruits, colors)}

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'green']
    print(create_fruit_color_dict(fruits, colors))