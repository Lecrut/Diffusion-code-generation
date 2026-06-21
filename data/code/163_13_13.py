def validate_input(fruits, colors):
    if not all(isinstance(item, str) for item in fruits + colors):
        raise ValueError("All elements must be strings")
    if len(fruits) != len(colors):
        raise ValueError("Fruits and colors lists must have the same length")

def create_fruit_color_dict(fruits, colors):
    validate_input(fruits, colors)
    return {fruit: color for fruit, color in zip(fruits, colors)}

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'green']
    fruit_color_dict = create_fruit_color_dict(fruits, colors)
    print(fruit_color_dict)