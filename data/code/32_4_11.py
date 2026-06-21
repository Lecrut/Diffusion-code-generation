def rectangle_area(width: float, height: float) -> float:
    if not isinstance(width, (int, float)):
        raise TypeError("width must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("height must be a number")
    if width < 0:
        raise ValueError("width must be non-negative")
    if height < 0:
        raise ValueError("height must be non-negative")
    return width * height

if __name__ == '__main__':
    print(rectangle_area(5, 10))
    print(rectangle_area(3.5, 2))
    print(rectangle_area(0, 10))
    print(rectangle_area(7, 0))