def calculate_rectangle_area(length, width):
    length = float(length)
    width = float(width)
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return length * width

if __name__ == '__main__':
    print(calculate_rectangle_area(5, 10))
    print(calculate_rectangle_area(3.5, 7.2))
    print(calculate_rectangle_area(0, 10))
    print(calculate_rectangle_area(100, 0))