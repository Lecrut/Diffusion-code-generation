import math

def calculate_area(shape_data):
    shape_type = shape_data.get("type")
    if shape_type == "circle":
        radius = shape_data.get("radius")
        if radius is None or radius < 0:
            raise ValueError("Circle requires a non-negative radius")
        return math.pi * radius ** 2
    elif shape_type == "rectangle":
        width = shape_data.get("width")
        height = shape_data.get("height")
        if width is None or height is None or width < 0 or height < 0:
            raise ValueError("Rectangle requires non-negative width and height")
        return width * height
    elif shape_type == "triangle":
        base = shape_data.get("base")
        height = shape_data.get("height")
        if base is None or height is None or base < 0 or height < 0:
            raise ValueError("Triangle requires non-negative base and height")
        return 0.5 * base * height
    elif shape_type == "square":
        side = shape_data.get("side")
        if side is None or side < 0:
            raise ValueError("Square requires a non-negative side length")
        return side ** 2
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    circle_params = {"type": "circle", "radius": 5}
    circle_area = calculate_area(circle_params)
    print(circle_area)

    rectangle_params = {"type": "rectangle", "width": 4, "height": 6}
    rectangle_area = calculate_area(rectangle_params)
    print(rectangle_area)

    triangle_params = {"type": "triangle", "base": 10, "height": 3}
    triangle_area = calculate_area(triangle_params)
    print(triangle_area)

    square_params = {"type": "square", "side": 4}
    square_area = calculate_area(square_params)
    print(square_area)