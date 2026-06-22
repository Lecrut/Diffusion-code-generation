def multiplication_grid():
    return [[i * j for j in range(1, 11)] for i in range(1, 11)]

if __name__ == '__main__':
    grid = multiplication_grid()
    print(grid)