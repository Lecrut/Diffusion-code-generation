def print_heart_pattern():
    coordinates = [
        (0, 2), (1, 1), (2, 0), (3, 0), (4, 1), (5, 2),
        (4, 3), (3, 4), (2, 4), (1, 3), (0, 2)
    ]
    for x, y in coordinates:
        print(f"\t{'*' if y == 0 else ' ' * x + '*'}", end='')
    print()

if __name__ == '__main__':
    print_heart_pattern()