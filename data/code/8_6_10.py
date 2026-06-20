import math

def calculate_area(shape_params):
    shape_type = shape_params.get("type")
    if shape_type == "circle":
        radius = shape_params.get("radius")
        return math.pi * radius * radius
    elif shape_type == "rectangle":
        width = shape_params.get("width")
        height = shape_params.get("height")
        return width * height
    elif shape_type == "triangle":
        base = shape_params.get("base")
        height = shape_params.get("height")
        return 0.5 * base * height
    elif shape_type == "square":
        side = shape_params.get("side")
        return side * side
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")

if __name__ == '__main__':
    circle_area = calculate_area({"type": "circle", "radius": 5})
    print(circle_area)

    rectangle_area = calculate_area({"type": "rectangle", "width": 4, "height": 6})
    print(rectangle_area)

    triangle_area = calculate_area({"type": "triangle", "base": 10, "height": 8})
    print(triangle_area)

    square_area = calculate_area({"type": "square", "side": 7})
    print(square_area)