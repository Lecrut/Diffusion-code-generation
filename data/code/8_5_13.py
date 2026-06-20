def calculate_area(shape, *dimensions):
    if shape == "rectangle":
        if len(dimensions) != 2:
            raise ValueError("Rectangle requires exactly 2 dimensions (width and height)")
        return dimensions[0] * dimensions[1]
    elif shape == "circle":
        if len(dimensions) != 1:
            raise ValueError("Circle requires exactly 1 dimension (radius)")
        import math
        return math.pi * (dimensions[0] ** 2)
    else:
        raise ValueError("Unsupported shape type. Use 'rectangle' or 'circle'.")

if __name__ == '__main__':
    sample_rectangle_area = calculate_area("rectangle", 5, 10)
    print(sample_rectangle_area)
    sample_circle_area = calculate_area("circle", 3)
    print(sample_circle_area)