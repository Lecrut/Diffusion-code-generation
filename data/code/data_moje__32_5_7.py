def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Arguments must be numeric.")
    return width * height

if __name__ == '__main__':
    width = 5
    height = 10
    area = calculate_rectangle_area(width, height)
    print(area)