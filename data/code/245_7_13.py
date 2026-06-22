import math
MATH_PI = math.pi

def calculate_ellipse_area(axes):
    semi_major_axis, semi_minor_axis = axes
    area = MATH_PI * semi_major_axis * semi_minor_axis
    return area

def calculate_rectangle_area(dimensions):
    length, width = dimensions
    area = length * width
    return area

def compare_areas(ellipse_axes, rectangle_dimensions):
    ellipse_area = calculate_ellipse_area(ellipse_axes)
    rectangle_area = calculate_rectangle_area(rectangle_dimensions)
    difference = abs(ellipse_area - rectangle_area)
    if difference == 0:
        print('The areas are equal.')
    else:
        print(f'The difference between the areas is: {difference}')
    return difference
if __name__ == '__main__':
    ellipse_data = (3, 4)
    rectangle_data = (6, 2)
    compare_areas(ellipse_data, rectangle_data)