def generate_square_grid():
    return {
        "0": {"0": True, "1": False, "2": True},
        "1": {"0": False, "1": True, "2": False},
        "2": {"0": True, "1": False, "2": True}
    }

if __name__ == '__main__':
    grid = generate_square_grid()
    print(grid)