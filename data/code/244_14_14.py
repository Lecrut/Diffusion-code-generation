def calculate_area(shape, dimension):
    if shape == 'circle':
        return 3.14 * (dimension ** 2)
    elif shape == 'square':
        return dimension ** 2
    else:
        raise ValueError("Unsupported shape")

def sum_of_areas(shape1, dimension1, shape2, dimension2):
    area1 = calculate_area(shape1, dimension1)
    area2 = calculate_area(shape2, dimension2)
    return area1 + area2

if __name__ == '__main__':
    total_area = sum_of_areas('circle', 5, 'square', 4)
    print(total_area)