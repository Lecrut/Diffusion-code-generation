def calculate_rectangle_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return width * height

if __name__ == '__main__':
    int_width = 5
    int_height = 3
    float_width = 4.5
    float_height = 2.1
    print(calculate_rectangle_area(int_width, int_height))
    print(calculate_rectangle_area(float_width, float_height))