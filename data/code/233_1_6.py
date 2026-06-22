def fill_rectangle(width, height):
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Width must be a positive integer")
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer")

    return ['#' * width for _ in range(height)]

if __name__ == '__main__':
    print(fill_rectangle(5, 3))