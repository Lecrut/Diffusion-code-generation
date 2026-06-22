def calculate_area(shape_type, dimension):
    if shape_type == 'circle':
        return 3.14 * (dimension ** 2)
    elif shape_type == 'square':
        return dimension ** 2
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    area_sum = calculate_area('circle', 5) + calculate_area('square', 4)
    print(area_sum)