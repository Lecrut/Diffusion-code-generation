def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numeric values")
    return width * height

if __name__ == '__main__':
    print(calculate_rectangle_area(5, 10))
    print(calculate_rectangle_area(3.5, 2))
    try:
        print(calculate_rectangle_area("5", 10))
    except TypeError as e:
        print(str(e))
    try:
        print(calculate_rectangle_area(5, None))
    except TypeError as e:
        print(str(e))