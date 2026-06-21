def generate_fruit_color_dict(fruits, colors):
    return {fruit: color for fruit, color in zip(fruits, colors)}

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'red']
    print(generate_fruit_color_dict(fruits, colors))