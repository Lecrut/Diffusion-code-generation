def merge_fruit_color_pairs(fruits, colors):
    if len(fruits) != len(colors):
        raise ValueError("Fruits and colors lists must have the same length")
    
    return {fruit: color for fruit, color in zip(fruits, colors)}

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'grape', 'orange']
    colors = ['red', 'yellow', 'purple', 'orange']
    
    try:
        merged_dict = merge_fruit_color_pairs(fruits, colors)
        print(merged_dict)
    except ValueError as e:
        print(e)