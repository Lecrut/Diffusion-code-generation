def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)):
        raise TypeError("Width must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if width < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return width * height

if __name__ == '__main__':
    w = 10
    h = 5
    result = calculate_rectangle_area(w, h)
    print(result)