def generate_grid():
    return {
        '0_0': False,
        '0_1': True,
        '0_2': False,
        '1_0': True,
        '1_1': False,
        '1_2': True,
        '2_0': False,
        '2_1': True,
        '2_2': False
    }

if __name__ == '__main__':
    grid = generate_grid()
    print(grid)