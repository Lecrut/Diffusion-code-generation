def calculate_area(shape_type, dimensions):
    if shape_type == 'rectangle':
        length, width = dimensions
        area = length * width
    elif shape_type == 'circle':
        radius = dimensions[0]
        area = 3.14159 * (radius ** 2)
    else:
        raise ValueError("Unsupported shape type")
    return area

if __name__ == '__main__':
    rectangle_dimensions = (5, 10)
    circle_dimensions = (7,)
    
    rectangle_area = calculate_area('rectangle', rectangle_dimensions)
    circle_area = calculate_area('circle', circle_dimensions)
    
    print(rectangle_area)
    print(circle_area)