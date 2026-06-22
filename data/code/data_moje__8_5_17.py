def calculate_area(shape_type, width=None, radius=None):
    if shape_type == "rectangle":
        return width * width
    elif shape_type == "circle":
        return 3.141592653589793 * (radius ** 2)
    return 0

if __name__ == '__main__':
    print(calculate_area("rectangle", width=5))
    print(calculate_area("circle", radius=3))