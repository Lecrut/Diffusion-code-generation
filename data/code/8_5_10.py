def calculate_area(shape_type, dim1, dim2=None):
    shape_type = shape_type.lower()
    if shape_type == 'rectangle':
        return dim1 * dim2
    if shape_type == 'circle':
        import math
        return math.pi * (dim1 ** 2)
    return 0

if __name__ == '__main__':
    print(calculate_area('rectangle', 5, 10))
    print(calculate_area('circle', 7))