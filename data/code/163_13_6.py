FRUITS = ['apple', 'banana', 'cherry']
COLORS = ['red', 'yellow', 'green']

def create_fruit_color_dict(fruits, colors):
    return {fruit: color for fruit, color in zip(fruits, colors)}

if __name__ == '__main__':
    fruit_color_dict = create_fruit_color_dict(FRUITS, COLORS)
    print(fruit_color_dict)