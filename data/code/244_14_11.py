def calculate_area(shape_type, dimension):
    if shape_type == 'circle':
        return 3.14 * dimension ** 2
    elif shape_type == 'square':
        return dimension ** 2
    else:
        raise ValueError("Unsupported shape type")

def sum_areas(shape1_type, shape1_dim, shape2_type, shape2_dim):
    area1 = calculate_area(shape1_type, shape1_dim)
    area2 = calculate_area(shape2_type, shape2_dim)
    return area1 + area2

if __name__ == '__main__':
    total_area = sum_areas('circle', 5, 'square', 3)
    print(total_area)