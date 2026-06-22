def generate_square_grid(N):
    return [[(i, j) for j in range(N)] for i in range(N)]

if __name__ == '__main__':
    grid = generate_square_grid(5)
    print(grid)