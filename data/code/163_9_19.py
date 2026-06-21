def merge_fruit_color_pairs(fruits, colors):
    if not (isinstance(fruits, list) and isinstance(colors, list)):
        raise ValueError("Both fruits and colors must be lists.")
    
    if len(fruits) != len(colors):
        raise ValueError("Fruits and colors lists must have the same length.")
    
    return {fruit: color for fruit, color in zip(fruits, colors)}

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'red']
    try:
        merged_dict = merge_fruit_color_pairs(fruits, colors)
        print(merged_dict)
    except ValueError as e:
        print(e)