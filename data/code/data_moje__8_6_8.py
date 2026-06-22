import math

def calculate_area(shape_params: dict) -> float:
    shape_type = shape_params.get("type")
    
    if shape_type == "circle":
        radius = shape_params.get("radius")
        if radius is None or radius <= 0:
            raise ValueError("Circle requires a positive 'radius'")
        return math.pi * radius ** 2
    
    if shape_type == "rectangle":
        width = shape_params.get("width")
        height = shape_params.get("height")
        if width is None or height is None or width <= 0 or height <= 0:
            raise ValueError("Rectangle requires positive 'width' and 'height'")
        return width * height
    
    if shape_type == "triangle":
        base = shape_params.get("base")
        height = shape_params.get("height")
        if base is None or height is None or base <= 0 or height <= 0:
            raise ValueError("Triangle requires positive 'base' and 'height'")
        return 0.5 * base * height
    
    if shape_type == "square":
        side = shape_params.get("side")
        if side is None or side <= 0:
            raise ValueError("Square requires a positive 'side'")
        return side ** 2
    
    if shape_type == "trapezoid":
        base1 = shape_params.get("base1")
        base2 = shape_params.get("base2")
        height = shape_params.get("height")
        if base1 is None or base2 is None or height is None or base1 <= 0 or base2 <= 0 or height <= 0:
            raise ValueError("Trapezoid requires positive 'base1', 'base2', and 'height'")
        return 0.5 * (base1 + base2) * height
    
    raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    circle_params = {"type": "circle", "radius": 5}
    rectangle_params = {"type": "rectangle", "width": 10, "height": 4}
    triangle_params = {"type": "triangle", "base": 6, "height": 8}
    square_params = {"type": "square", "side": 7}
    trapezoid_params = {"type": "trapezoid", "base1": 3, "base2": 7, "height": 5}

    print(calculate_area(circle_params))
    print(calculate_area(rectangle_params))
    print(calculate_area(triangle_params))
    print(calculate_area(square_params))
    print(calculate_area(trapezoid_params))