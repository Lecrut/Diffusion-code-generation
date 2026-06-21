def rectangle_area(width, height):
    if not isinstance(width, (int, float)):
        raise TypeError("width must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("height must be a number")
    return width * height

if __name__ == '__main__':
    result = rectangle_area(5, 10)
    print(result)