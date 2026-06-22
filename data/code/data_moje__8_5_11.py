import math

def calculate_area(shape_type, dimensions):
    if shape_type.lower() == "rectangle":
        width, height = dimensions
        return width * height
    elif shape_type.lower() == "circle":
        radius = dimensions
        return math.pi * radius ** 2
    else:
        raise ValueError("Unsupported shape type. Use 'rectangle' or 'circle'.")

if __name__ == "__main__":
    rect_result = calculate_area("rectangle", (5, 10))
    print(rect_result)

    circle_result = calculate_area("circle", 7)
    print(circle_result)