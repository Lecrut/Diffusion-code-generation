def generate_square_grid():
    return {
        (0, 0): True,
        (0, 1): False,
        (0, 2): True,
        (1, 0): False,
        (1, 1): True,
        (1, 2): False,
        (2, 0): True,
        (2, 1): False,
        (2, 2): True
    }

if __name__ == '__main__':
    grid = generate_square_grid()
    print(grid)