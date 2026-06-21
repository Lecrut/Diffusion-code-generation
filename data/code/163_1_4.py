def create_fruit_color_pairs():
    fruits = ["apple", "banana", "cherry"]
    colors = ["red", "yellow", "red"]
    pairs = list(zip(fruits, colors))
    return pairs

if __name__ == '__main__':
    fruit_color_pairs = create_fruit_color_pairs()
    print(fruit_color_pairs)