def calculate_area(shape_type, dimension):
    if shape_type == 'circle':
        return 3.14 * (dimension ** 2)
    elif shape_type == 'square':
        return dimension ** 2
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    circle_area = calculate_area('circle', 5)
    square_area = calculate_area('square', 3)
    total_area = circle_area + square_area
    print(total_area)