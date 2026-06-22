def generate_square_grid(N):
    perimeter = set()
    for i in range(N):
        perimeter.add((i, 0))
        perimeter.add((N-1, i))
        perimeter.add((i, N-1))
        perimeter.add((0, i))
    return perimeter

if __name__ == '__main__':
    grid_size = 10
    perimeter_points = generate_square_grid(grid_size)
    for point in perimeter_points:
        print(point)