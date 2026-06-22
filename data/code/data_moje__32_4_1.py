def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)):
        raise TypeError("width must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("height must be a number")
    if width < 0 or height < 0:
        raise ValueError("width and height must be non-negative")
    return width * height

if __name__ == '__main__':
    print(calculate_rectangle_area(5, 10))