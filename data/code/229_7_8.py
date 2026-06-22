def generate_grid():
    return {
        '0': {'0': False, '1': True, '2': False},
        '1': {'0': True, '1': False, '2': True},
        '2': {'0': False, '1': True, '2': False}
    }

if __name__ == '__main__':
    grid = generate_grid()
    print(grid)