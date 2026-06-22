def rectangle_area(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numeric types")
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return length * width

if __name__ == '__main__':
    length = 5
    width = 10.5
    area = rectangle_area(length, width)
    print(area)