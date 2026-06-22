def create_plus_grid(size):
    row = "+" * size + "\n"
    grid = row * size
    return grid

if __name__ == '__main__':
    result = create_plus_grid(10)
    print(result)