def merge_fruit_color_pairs(fruits, colors):
    return {fruits[i]: colors[i] for i in range(len(fruits))}

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'red']
    print(merge_fruit_color_pairs(fruits, colors))