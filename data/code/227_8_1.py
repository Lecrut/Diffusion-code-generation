def print_heart_star():
    coordinates = [
        (0, 2), (1, 3), (2, 4), (3, 5), (4, 6),
        (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)
    ]
    for x, y in coordinates:
        print('*' * (y + 1))

if __name__ == '__main__':
    print_heart_star()