def validate_input(fruits, colors):
    if not fruits or not colors:
        raise ValueError("Both fruits and colors must be non-empty lists.")
    if len(fruits) != len(colors):
        raise ValueError("Fruits and colors lists must have the same length.")

def create_fruit_color_pairs():
    fruits = ["apple", "banana", "cherry"]
    colors = ["red", "yellow", "red"]
    
    validate_input(fruits, colors)
    
    return list(zip(fruits, colors))

if __name__ == '__main__':
    fruit_color_pairs = create_fruit_color_pairs()
    print(fruit_color_pairs)