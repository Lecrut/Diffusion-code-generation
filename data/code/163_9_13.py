FRUIT_COLORS = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple",
    "orange": "orange"
}

def merge_fruit_color_pairs(fruits, colors):
    return {fruit: color for fruit, color in zip(fruits, colors)}

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'red']
    merged_dict = merge_fruit_color_pairs(fruits, colors)
    print(merged_dict)