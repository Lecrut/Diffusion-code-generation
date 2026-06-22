def circle_area(radius):
    return 3.14159 * radius ** 2

def rectangle_area(width, height):
    return width * height

def shapes_equal_area(circle_radius, rect_width, rect_height):
    return circle_area(circle_radius) == rectangle_area(rect_width, rect_height)

if __name__ == '__main__':
    print(shapes_equal_area(5, 10, 3.14))