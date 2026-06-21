def create_fruit_color_pairs():
    fruits = ["apple", "banana", "cherry"]
    colors = ["red", "yellow", "red"]
    fruit_color_pairs = list(zip(fruits, colors))
    return fruit_color_pairs

if __name__ == '__main__':
    pairs = create_fruit_color_pairs()
    print(pairs)