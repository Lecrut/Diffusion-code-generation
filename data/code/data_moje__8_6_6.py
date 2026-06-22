import math

def calculate_area(shape_params: dict) -> float:
    shape_type = shape_params.get("shape")
    if shape_type == "circle":
        radius = shape_params.get("radius")
        if radius is None or radius < 0:
            raise ValueError("Circle must have a valid non-negative radius.")
        return math.pi * radius ** 2
    elif shape_type == "rectangle":
        width = shape_params.get("width")
        height = shape_params.get("height")
        if width is None or height is None or width < 0 or height < 0:
            raise ValueError("Rectangle must have valid non-negative width and height.")
        return width * height
    elif shape_type == "triangle":
        base = shape_params.get("base")
        height = shape_params.get("height")
        if base is None or height is None or base < 0 or height < 0:
            raise ValueError("Triangle must have valid non-negative base and height.")
        return 0.5 * base * height
    elif shape_type == "square":
        side = shape_params.get("side")
        if side is None or side < 0:
            raise ValueError("Square must have a valid non-negative side.")
        return side ** 2
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    circle_params = {"shape": "circle", "radius": 5}
    print(calculate_area(circle_params))

    rectangle_params = {"shape": "rectangle", "width": 4, "height": 6}
    print(calculate_area(rectangle_params))

    triangle_params = {"shape": "triangle", "base": 10, "height": 5}
    print(calculate_area(triangle_params))

    square_params = {"shape": "square", "side": 3}
    print(calculate_area(square_params))