def merge_fruit_color_pairs(fruits, colors):
    return dict(zip(fruits, colors))

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'grape', 'orange']
    colors = ['red', 'yellow', 'purple', 'orange']
    merged_dict = merge_fruit_color_pairs(fruits, colors)
    print(merged_dict)