def calculate_area(shape_type, dimension):
    if shape_type == 'circle':
        return 3.14 * (dimension ** 2)
    elif shape_type == 'square':
        return dimension ** 2
    else:
        raise ValueError("Unsupported shape type")

def sum_of_areas(shape1_type, dimension1, shape2_type, dimension2):
    area1 = calculate_area(shape1_type, dimension1)
    area2 = calculate_area(shape2_type, dimension2)
    return area1 + area2

if __name__ == '__main__':
    print(sum_of_areas('circle', 5, 'square', 4))