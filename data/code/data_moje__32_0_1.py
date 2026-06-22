def calculate_rectangle_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative.")
    return width * height

if __name__ == '__main__':
    width = 5
    height = 10
    result = calculate_rectangle_area(width, height)
    print(result)