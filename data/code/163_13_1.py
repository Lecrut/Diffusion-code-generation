def create_fruit_color_dict(fruits, colors):
    return {fruit: color for fruit, color in zip(fruits, colors)}

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'red']
    print(create_fruit_color_dict(fruits, colors))