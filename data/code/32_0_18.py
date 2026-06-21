def calculate_rectangle_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative")
    return width * height

if __name__ == '__main__':
    print(calculate_rectangle_area(5, 10))
    print(calculate_rectangle_area(3.5, 2))
    try:
        calculate_rectangle_area(-1, 5)
    except ValueError as e:
        print(e)