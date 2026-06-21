def rectangle_area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numeric types.")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive numbers.")
    return width * height

if __name__ == '__main__':
    result = rectangle_area(5, 10)
    print(result)