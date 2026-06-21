def create_fruit_color_dict(fruits, colors):
    if not all(isinstance(item, str) for item in fruits + colors):
        raise ValueError("All elements must be strings.")
    return {fruit: color for fruit, color in zip(fruits, colors)}

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'green']
    try:
        fruit_color_dict = create_fruit_color_dict(fruits, colors)
        print(fruit_color_dict)
    except ValueError as e:
        print(e)