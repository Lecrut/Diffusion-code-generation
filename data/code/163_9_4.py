def merge_fruit_color_pairs(fruits, colors):
    return {**fruits, **colors}

if __name__ == '__main__':
    fruits = {'apple': 'red', 'banana': 'yellow'}
    colors = {'red': 'stop', 'green': 'go'}
    merged_dict = merge_fruit_color_pairs(fruits, colors)
    print(merged_dict)