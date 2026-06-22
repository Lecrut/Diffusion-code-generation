def generate_grid(width, height):
    return ['#' * width for _ in range(height)]

if __name__ == '__main__':
    print(generate_grid(3, 2))