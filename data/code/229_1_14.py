def generate_coordinate_grid(N):
    return [[(i, j) for j in range(N)] for i in range(N)]

if __name__ == '__main__':
    grid = generate_coordinate_grid(5)
    for row in grid:
        print(row)