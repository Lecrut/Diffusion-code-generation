def calculate_area(shape_type, dimensions):
    if shape_type == "rectangle":
        width, height = dimensions
        return width * height
    elif shape_type == "circle":
        radius = dimensions
        return 3.141592653589793 * radius ** 2
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rect_area = calculate_area("rectangle", (5, 10))
    circle_area = calculate_area("circle", 7)
    print(rect_area)
    print(circle_area)