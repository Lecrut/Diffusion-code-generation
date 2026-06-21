def rectangle_area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numbers")
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative")
    return width * height

if __name__ == '__main__':
    print(rectangle_area(5, 10))
    print(rectangle_area(3.5, 2.0))
    try:
        print(rectangle_area('a', 10))
    except TypeError as e:
        print("TypeError:", e)
    try:
        print(rectangle_area(-1, 10))
    except ValueError as e:
        print("ValueError:", e)