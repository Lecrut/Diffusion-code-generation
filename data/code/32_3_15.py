def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numbers.")
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative.")
    return width * height

if __name__ == '__main__':
    w = 5
    h = 10
    result = calculate_rectangle_area(w, h)
    print(result)
    w2 = 0
    h2 = 7
    result2 = calculate_rectangle_area(w2, h2)
    print(result2)