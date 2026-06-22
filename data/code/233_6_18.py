def checkerboard(width, height):
    for y in range(height):
        line = ''.join(['#' if (x + y) % 2 else '.' for x in range(width)])
        print(line)

if __name__ == '__main__':
    checkerboard(8, 8)