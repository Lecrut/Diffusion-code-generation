def calculate_area(shape, dimension):
    if shape == 'circle':
        return 3.14159 * (dimension ** 2)
    elif shape == 'square':
        return dimension ** 2
    else:
        raise ValueError("Unsupported shape")

def sum_areas(circle_radius, square_side):
    circle_area = calculate_area('circle', circle_radius)
    square_area = calculate_area('square', square_side)
    return circle_area + square_area

if __name__ == '__main__':
    total_area = sum_areas(3, 4)
    print(total_area)