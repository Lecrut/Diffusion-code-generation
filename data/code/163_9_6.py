def merge_fruit_color_pairs(fruits, colors):
    return {fruit: color for fruit, color in zip(fruits, colors)}

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'grape']
    colors = ['red', 'yellow', 'purple']
    merged_dict = merge_fruit_color_pairs(fruits, colors)
    print(merged_dict)