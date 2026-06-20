def calculate_area(shape_params: dict) -> float:
    shape_type = shape_params.get("type")
    if shape_type == "circle":
        radius = shape_params.get("radius")
        if radius is None or radius <= 0:
            raise ValueError("Invalid radius for circle")
        return 3.14159265359 * radius * radius
    elif shape_type == "rectangle":
        width = shape_params.get("width")
        height = shape_params.get("height")
        if width is None or height is None or width <= 0 or height <= 0:
            raise ValueError("Invalid dimensions for rectangle")
        return width * height
    elif shape_type == "triangle":
        base = shape_params.get("base")
        height = shape_params.get("height")
        if base is None or height is None or base <= 0 or height <= 0:
            raise ValueError("Invalid dimensions for triangle")
        return 0.5 * base * height
    elif shape_type == "square":
        side = shape_params.get("side")
        if side is None or side <= 0:
            raise ValueError("Invalid side length for square")
        return side * side
    elif shape_type == "trapezoid":
        base_a = shape_params.get("base_a")
        base_b = shape_params.get("base_b")
        height = shape_params.get("height")
        if base_a is None or base_b is None or height is None or base_a <= 0 or base_b <= 0 or height <= 0:
            raise ValueError("Invalid dimensions for trapezoid")
        return 0.5 * (base_a + base_b) * height
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    circle_area = calculate_area({"type": "circle", "radius": 5})
    print(circle_area)
    rect_area = calculate_area({"type": "rectangle", "width": 10, "height": 4})
    print(rect_area)
    tri_area = calculate_area({"type": "triangle", "base": 6, "height": 3})
    print(tri_area)
    square_area = calculate_area({"type": "square", "side": 7})
    print(square_area)
    trap_area = calculate_area({"type": "trapezoid", "base_a": 3, "base_b": 7, "height": 5})
    print(trap_area)