def create_fruit_color_dict(fruits, colors):
    if not isinstance(fruits, list) or not isinstance(colors, list):
        raise ValueError("Both fruits and colors must be lists.")
    
    if len(fruits) != len(colors):
        raise ValueError("Fruits and colors lists must have the same length.")
    
    return {fruit: color for fruit, color in zip(fruits, colors)}

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'green']
    try:
        fruit_color_dict = create_fruit_color_dict(fruits, colors)
        print(fruit_color_dict)
    except ValueError as e:
        print(e)