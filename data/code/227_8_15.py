def print_heart_star():
    coordinates = [
        (0, 2), (1, 3), (2, 4), (3, 5), (4, 6),
        (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)
    ]
    
    def draw_star(x, y):
        if x < len(coordinates) and y >= coordinates[x][1]:
            print('*' * (coordinates[x][1] + 1))
        else:
            print(' ' * (coordinates[-1][1] + 1))

    for x in range(len(coordinates)):
        draw_star(x, 0)

if __name__ == '__main__':
    print_heart_star()