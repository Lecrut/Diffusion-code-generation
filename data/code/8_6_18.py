import math

def calculate_area(shape_dict):
    shape_type = shape_dict.get("type")
    if shape_type == "circle":
        radius = shape_dict.get("radius", 0)
        return math.pi * radius ** 2
    elif shape_type == "rectangle":
        width = shape_dict.get("width", 0)
        height = shape_dict.get("height", 0)
        return width * height
    elif shape_type == "triangle":
        base = shape_dict.get("base", 0)
        height = shape_dict.get("height", 0)
        return 0.5 * base * height
    elif shape_type == "square":
        side = shape_dict.get("side", 0)
        return side ** 2
    elif shape_type == "trapezoid":
        a = shape_dict.get("a", 0)
        b = shape_dict.get("b", 0)
        height = shape_dict.get("height", 0)
        return 0.5 * (a + b) * height
    elif shape_type == "ellipse":
        a = shape_dict.get("a", 0)
        b = shape_dict.get("b", 0)
        return math.pi * a * b
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")

if __name__ == '__main__':
    circle_shape = {"type": "circle", "radius": 5}
    rectangle_shape = {"type": "rectangle", "width": 4, "height": 6}
    triangle_shape = {"type": "triangle", "base": 3, "height": 4}
    square_shape = {"type": "square", "side": 7}
    trapezoid_shape = {"type": "trapezoid", "a": 5, "b": 3, "height": 4}
    ellipse_shape = {"type": "ellipse", "a": 5, "b": 3}

    print(calculate_area(circle_shape))
    print(calculate_area(rectangle_shape))
    print(calculate_area(triangle_shape))
    print(calculate_area(square_shape))
    print(calculate_area(trapezoid_shape))
    print(calculate_area(ellipse_shape))