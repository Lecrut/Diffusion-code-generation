def print_heart_star():
    coordinates = [
        (0, 2), (1, 3), (2, 4), (3, 5), (4, 6),
        (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)
    ]
    max_width = max(x + y for x, y in coordinates) * 2
    for x, y in coordinates:
        line = ' ' * ((max_width // 2) - (x + y)) + '*' * (y * 2 + 1)
        print(line)

if __name__ == '__main__':
    print_heart_star()