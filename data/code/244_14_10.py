def calculate_area(shape_type, dimension):
    if shape_type == 'circle':
        return 3.14 * (dimension ** 2)
    elif shape_type == 'square':
        return dimension ** 2
    else:
        raise ValueError("Unsupported shape type")

def sum_areas(circle_radius, square_side):
    circle_area = calculate_area('circle', circle_radius)
    square_area = calculate_area('square', square_side)
    return circle_area + square_area

if __name__ == '__main__':
    print(sum_areas(3, 4))