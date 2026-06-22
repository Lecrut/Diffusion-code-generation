import math

def calculate_area(shape_type, dimensions):
    if shape_type == "rectangle":
        if len(dimensions) != 2:
            raise ValueError("Rectangle requires length and width")
        length, width = dimensions
        return length * width
    elif shape_type == "circle":
        if len(dimensions) != 1:
            raise ValueError("Circle requires radius")
        radius = dimensions[0]
        return math.pi * radius * radius
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle_shape = "rectangle"
    rectangle_dims = [5, 10]
    circle_shape = "circle"
    circle_dims = [3]
    
    rect_area = calculate_area(rectangle_shape, rectangle_dims)
    circ_area = calculate_area(circle_shape, circle_dims)
    
    print(rect_area)
    print(circ_area)