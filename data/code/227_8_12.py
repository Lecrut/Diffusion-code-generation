def print_heart_star():
    coordinates = {
        0: (2,), 1: (3,), 2: (4,), 3: (5,), 4: (6,),
        5: (5,), 6: (4,), 7: (3,), 8: (2,), 9: (1,)
    }
    for x, y in coordinates.items():
        print('*' * (y[0] + 1))

if __name__ == '__main__':
    print_heart_star()