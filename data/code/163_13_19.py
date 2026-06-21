def validate_input(fruits, colors):
    if not isinstance(fruits, list) or not isinstance(colors, list):
        raise ValueError("Inputs must be lists")
    if len(fruits) != len(colors):
        raise ValueError("Fruits and colors lists must have the same length")

def create_fruit_color_dict(fruits, colors):
    validate_input(fruits, colors)
    return {fruit: color for fruit, color in zip(fruits, colors)}

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'green']
    print(create_fruit_color_dict(fruits, colors))