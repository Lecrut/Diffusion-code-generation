def display_square(side):
    for i in range(side):
        print("=" * (side * 2))
        for j in range(side):
            print("* ", end="")
        print()
        if i < side - 1:
            print("-" * (side * 2))
if __name__ == '__main__':
    side_length = 5
    display_square(side_length)