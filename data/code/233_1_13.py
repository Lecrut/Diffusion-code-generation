def generate_hash_grid(width, height):
    return ['#' * width for _ in range(height)]

if __name__ == '__main__':
    grid = generate_hash_grid(5, 3)
    print(grid)