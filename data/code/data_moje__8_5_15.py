def calculate_area(shape, *dimensions):
    if shape == "rectangle":
        if len(dimensions) != 2:
            raise ValueError("Rectangle requires length and width")
        length, width = dimensions
        return length * width
    elif shape == "circle":
        if len(dimensions) != 1:
            raise ValueError("Circle requires radius")
        radius = dimensions[0]
        return 3.14159 * radius * radius
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    shape_type = "rectangle"
    length_val = 5
    width_val = 10
    radius_val = 3
    
    rect_area = calculate_area(shape_type, length_val, width_val)
    print(rect_area)
    
    shape_type = "circle"
    circ_area = calculate_area(shape_type, radius_val)
    print(circ_area)