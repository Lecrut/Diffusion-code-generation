def rectangle_area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numeric types")
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative")
    return width * height

if __name__ == '__main__':
    result = rectangle_area(5, 10)
    print(result)
    result2 = rectangle_area(3.5, 4.2)
    print(result2)
    try:
        rectangle_area('a', 10)
    except TypeError as e:
        print(e)
    try:
        rectangle_area(-1, 5)
    except ValueError as e:
        print(e)