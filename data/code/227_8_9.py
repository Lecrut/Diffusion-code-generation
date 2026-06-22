def print_heart_star_pattern():
    coordinates = [
        (0, 2), (1, 3), (2, 4), (3, 5), (4, 6),
        (4, 7), (3, 8), (2, 9), (1, 10), (0, 11),
        (-1, 10), (-2, 9), (-3, 8), (-4, 7), (-4, 6),
        (-3, 5), (-2, 4), (-1, 3)
    ]
    for x, y in coordinates:
        print('*' if abs(x) + abs(y) <= 4 else ' ', end='')
    print()

if __name__ == '__main__':
    print_heart_star_pattern()