FRUITS = ["apple", "banana", "cherry"]
COLORS = ["red", "yellow", "red"]

def create_fruit_color_pairs():
    return list(zip(FRUITS, COLORS))

if __name__ == '__main__':
    fruit_color_pairs = create_fruit_color_pairs()
    print(fruit_color_pairs)