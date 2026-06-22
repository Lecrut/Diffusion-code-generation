def generate_checkerboard(width, height):
    return '\n'.join([''.join(['#' if (i + j) % 2 else '.' for i in range(width)]) for j in range(height)])

if __name__ == '__main__':
    print(generate_checkerboard(8, 4))