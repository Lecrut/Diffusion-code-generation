def create_fruit_color_pairs():
    fruits = ["apple", "banana", "cherry"]
    colors = ["red", "yellow", "red"]
    
    if len(fruits) != len(colors):
        raise ValueError("Fruits and colors lists must have the same length")
    
    return list(zip(fruits, colors))

if __name__ == '__main__':
    pairs = create_fruit_color_pairs()
    print(pairs)