def calculate_area(shape_type, width=None, radius=None):
    shape_type = shape_type.lower()
    if shape_type == "rectangle":
        if width is None or width <= 0:
            raise ValueError("Rectangle requires a positive width.")
        height = width
        return width * height
    elif shape_type == "circle":
        if radius is None or radius <= 0:
            raise ValueError("Circle requires a positive radius.")
        import math
        return math.pi * (radius ** 2)
    else:
        raise ValueError("Unsupported shape type. Use 'rectangle' or 'circle'.")

if __name__ == '__main__':
    rectangle_area = calculate_area("rectangle", width=5)
    print(rectangle_area)

    circle_area = calculate_area("circle", radius=3)
    print(circle_area)