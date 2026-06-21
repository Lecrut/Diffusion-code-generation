def merge_fruit_color_pairs(fruits, colors):
    return {fruits[i]: colors[i] for i in range(min(len(fruits), len(colors)))}

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'red']
    merged_dict = merge_fruit_color_pairs(fruits, colors)
    print(merged_dict)