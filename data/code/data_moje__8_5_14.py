def calculate_area(shape, dimensions):
    if shape == "rectangle":
        length, width = dimensions
        return length * width
    elif shape == "circle":
        radius = dimensions
        return 3.141592653589793 * radius ** 2
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rect_area = calculate_area("rectangle", (5, 10))
    print(rect_area)
    circle_area = calculate_area("circle", (7))
    print(circle_area)