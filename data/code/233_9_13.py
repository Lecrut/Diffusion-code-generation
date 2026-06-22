def generate_rectangle(width=8, height=8):
    rectangle = [['#' for _ in range(width)] for _ in range(height)]
    return rectangle

if __name__ == '__main__':
    sample_grid = generate_rectangle(7, 6)
    print(sample_grid)