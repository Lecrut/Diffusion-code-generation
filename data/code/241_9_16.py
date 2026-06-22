def calculate_area(length, width):
    if not all(isinstance(i, (int, float)) for i in [length, width]):
        raise ValueError("Both length and width must be numbers")
    return length * width

if __name__ == '__main__':
    rectangle_length = 7
    rectangle_width = 4
    area = calculate_area(rectangle_length, rectangle_width)
    print(area)