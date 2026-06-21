def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)) or isinstance(width, bool):
        raise TypeError("Width must be a numeric value")
    if not isinstance(height, (int, float)) or isinstance(height, bool):
        raise TypeError("Height must be a numeric value")
    return width * height

if __name__ == '__main__':
    area = calculate_rectangle_area(5, 10)
    print(area)
    try:
        calculate_rectangle_area("5", 10)
    except TypeError as e:
        print(e)