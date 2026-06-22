def print_heart_star():
    coordinates = [
        (0, 1), (1, 2), (2, 3), (3, 4),
        (4, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)
    ]
    for x, y in coordinates:
        print('*' * (y + 1))

if __name__ == '__main__':
    print_heart_star()