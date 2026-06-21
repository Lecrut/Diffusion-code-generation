def calculate_rectangle_area(width, height):
    return width * height

if __name__ == '__main__':
    int_width = 5
    int_height = 10
    float_width = 4.5
    float_height = 2.3
    print(calculate_rectangle_area(int_width, int_height))
    print(calculate_rectangle_area(float_width, float_height))