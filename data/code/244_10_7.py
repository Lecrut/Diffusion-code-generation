def area_circle(radius):
    return 3.14159 * radius ** 2

def area_rectangle(length, width):
    return length * width

def sum_areas(circle_radius, rectangle_length, rectangle_width):
    circle_area = area_circle(circle_radius)
    rectangle_area = area_rectangle(rectangle_length, rectangle_width)
    return circle_area + rectangle_area

if __name__ == '__main__':
    print(sum_areas(5, 10, 2))