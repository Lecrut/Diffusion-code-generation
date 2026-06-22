def calculate_area(shape_type, dimension):
    if shape_type == 'circle':
        area = 3.14 * (dimension ** 2)
    elif shape_type == 'square':
        area = dimension ** 2
    else:
        raise ValueError("Unsupported shape type")
    return area

if __name__ == '__main__':
    circle_area = calculate_area('circle', 5)
    square_area = calculate_area('square', 4)
    total_area = circle_area + square_area
    print(total_area)