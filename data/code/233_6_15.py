def generate_checkerboard(width: int, height: int) -> str:
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers")

    checkerboard = []
    for y in range(height):
        row = ''.join(['#' if (x + y) % 2 else '.' for x in range(width)])
        checkerboard.append(row)
    
    return '\n'.join(checkerboard)

if __name__ == '__main__':
    width, height = 8, 6
    print(generate_checkerboard(width, height))