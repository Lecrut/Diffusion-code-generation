def rectangle_area(width, height):
    if not isinstance(width, (int, float)) or isinstance(width, bool):
        raise TypeError("width must be a number")
    if not isinstance(height, (int, float)) or isinstance(height, bool):
        raise TypeError("height must be a number")
    return width * height

if __name__ == '__main__':
    print(rectangle_area(5, 10))
    print(rectangle_area(3.5, 4.2))