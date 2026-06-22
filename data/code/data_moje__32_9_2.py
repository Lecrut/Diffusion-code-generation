def rectangle_area(width, height):
    if not isinstance(width, (int, float)):
        raise TypeError("Width must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if width < 0:
        raise ValueError("Width must be non-negative")
    if height < 0:
        raise ValueError("Height must be non-negative")
    return width * height

if __name__ == '__main__':
    print(rectangle_area(5, 10))
    print(rectangle_area(0, 10))
    print(rectangle_area(3.5, 2.0))
    try:
        rectangle_area(-1, 5)
    except ValueError as e:
        print(e)
    try:
        rectangle_area("5", 10)
    except TypeError as e:
        print(e)