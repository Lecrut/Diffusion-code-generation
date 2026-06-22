def rectangle_area(width: float, height: float) -> float:
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("width and height must be numbers")
    if width < 0 or height < 0:
        raise ValueError("width and height must be non-negative")
    return width * height

if __name__ == '__main__':
    print(rectangle_area(5, 10))
    print(rectangle_area(3.5, 2))
    print(rectangle_area(0, 10))