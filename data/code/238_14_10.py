def create_box(symbol, width, height):
    if not isinstance(symbol, str) or len(symbol) != 1:
        raise ValueError("Symbol must be a single character.")
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Width must be a positive integer.")
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer.")

    box = symbol * width + '\n' * (height - 1)
    return box

if __name__ == '__main__':
    box = create_box('@', 3, 2)
    print(box)