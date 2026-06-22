def calculate_area(shape, dimensions):
    if shape == "rectangle":
        length = dimensions.get("length", 0)
        width = dimensions.get("width", 0)
        return length * width
    elif shape == "circle":
        radius = dimensions.get("radius", 0)
        return 3.14159 * radius * radius
    else:
        return 0

if __name__ == '__main__':
    sample_rectangle = calculate_area("rectangle", {"length": 5, "width": 3})
    sample_circle = calculate_area("circle", {"radius": 2})
    print(sample_rectangle)
    print(sample_circle)