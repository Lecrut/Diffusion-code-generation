def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)):
        raise TypeError("Width must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive numbers")
    return width * height

if __name__ == '__main__':
    try:
        w = 5
        h = 10
        area = calculate_rectangle_area(w, h)
        print(area)
    except (TypeError, ValueError) as e:
        print(e)