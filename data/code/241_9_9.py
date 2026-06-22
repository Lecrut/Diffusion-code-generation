def calculate_area(length, width):
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        raise ValueError("Both length and width must be numbers.")
    return length * width

if __name__ == '__main__':
    rectangle_length = 7.5
    rectangle_width = 4.2
    area = calculate_area(rectangle_length, rectangle_width)
    print(area)