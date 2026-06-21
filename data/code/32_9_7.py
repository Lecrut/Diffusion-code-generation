def get_rectangle_area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numeric values")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive values")
    return width * height

if __name__ == '__main__':
    w = 5
    h = 10
    print(get_rectangle_area(w, h))