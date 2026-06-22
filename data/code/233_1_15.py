def generate_hash_grid(width, height):
    if width < 1 or height < 1:
        raise ValueError("Width and height must be positive integers.")
    
    return ['#' * width for _ in range(height)]

if __name__ == '__main__':
    grid = generate_hash_grid(5, 3)
    for row in grid:
        print(row)