def rectangle_area(length, width):
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        raise TypeError("Length and width must be numbers.")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

if __name__ == '__main__':
    try:
        area = rectangle_area(5, 3)
        print(area)
    except (TypeError, ValueError) as e:
        print(e)