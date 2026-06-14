def display_square(side):
    for i in range(side):
        print("=" * (side * 2))
        for j in range(side):
            print("* ", end="")
        print()
        print("=" * (side * 2))
if __name__ == '__main__':
    sample_side = 5
    display_square(sample_side)