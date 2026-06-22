def create_multiplication_grid(size=10):
    if size <= 0:
        raise ValueError("Grid size must be a positive integer")
    return [[(r + 1) * (c + 1) for c in range(size)] for r in range(size)]

if __name__ == '__main__':
    GRID_LIMIT = 10
    result = create_multiplication_grid(GRID_LIMIT)
    for row in result:
        print(row)