def create_fruit_color_pairs():
    fruits = ["apple", "banana", "cherry"]
    colors = ["red", "yellow", "red"]
    return list(zip(fruits, colors))

if __name__ == '__main__':
    pairs = create_fruit_color_pairs()
    print(pairs)