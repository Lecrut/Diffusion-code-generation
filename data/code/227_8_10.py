class HeartPattern:
    HEART_COORDINATES = [
        (0, 2), (1, 3), (2, 4), (3, 5), (4, 6),
        (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)
    ]

    @staticmethod
    def print_heart_star():
        for x, y in HeartPattern.HEART_COORDINATES:
            print('*' * (y + 1))

if __name__ == '__main__':
    HeartPattern.print_heart_star()