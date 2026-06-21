def create_fruit_color_dict(fruits, colors):
    fruit_color_dict = {}
    for fruit, color in zip(fruits, colors):
        if fruit in fruit_color_dict:
            print(f"Collision detected: {fruit} already has a value.")
        else:
            fruit_color_dict[fruit] = color
    return fruit_color_dict

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'red']
    print(create_fruit_color_dict(fruits, colors))