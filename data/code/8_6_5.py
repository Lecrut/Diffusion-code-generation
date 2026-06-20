import math

def calculate_area(shape_spec):
    shape_type = shape_spec.get("type")
    if shape_type == "circle":
        radius = shape_spec.get("radius", 0)
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius ** 2
    elif shape_type == "rectangle":
        width = shape_spec.get("width", 0)
        height = shape_spec.get("height", 0)
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative")
        return width * height
    elif shape_type == "triangle":
        base = shape_spec.get("base", 0)
        height = shape_spec.get("height", 0)
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative")
        return 0.5 * base * height
    elif shape_type == "square":
        side = shape_spec.get("side", 0)
        if side < 0:
            raise ValueError("Side length cannot be negative")
        return side ** 2
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    circle_spec = {"type": "circle", "radius": 5}
    rectangle_spec = {"type": "rectangle", "width": 4, "height": 6}
    triangle_spec = {"type": "triangle", "base": 3, "height": 4}
    square_spec = {"type": "square", "side": 7}

    print(calculate_area(circle_spec))
    print(calculate_area(rectangle_spec))
    print(calculate_area(triangle_spec))
    print(calculate_area(square_spec))