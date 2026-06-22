def generate_grid(width, height):
    return ['#' * width for _ in range(height)]

if __name__ == '__main__':
    grid = generate_grid(5, 3)
    for row in grid:
        print(row)