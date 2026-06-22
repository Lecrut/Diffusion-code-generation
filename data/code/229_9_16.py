N = 10

def create_square_grid(N):
    perimeter_points = set()
    for i in range(N):
        perimeter_points.add((i, 0))
        perimeter_points.add((i, N-1))
        perimeter_points.add((0, i))
        perimeter_points.add((N-1, i))
    return list(perimeter_points)

if __name__ == '__main__':
    result_grid = create_square_grid(N)
    print(result_grid)