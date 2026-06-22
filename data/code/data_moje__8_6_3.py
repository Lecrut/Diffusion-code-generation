import math

def calculate_area(shape_params: dict) -> float:
    shape_type = shape_params.get("type")
    
    if shape_type == "circle":
        radius = shape_params.get("radius", 0)
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius * radius
    
    elif shape_type == "rectangle":
        width = shape_params.get("width", 0)
        height = shape_params.get("height", 0)
        if width < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative")
        return width * height
    
    elif shape_type == "triangle":
        base = shape_params.get("base", 0)
        height = shape_params.get("height", 0)
        if base < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative")
        return 0.5 * base * height
    
    elif shape_type == "trapezoid":
        base1 = shape_params.get("base1", 0)
        base2 = shape_params.get("base2", 0)
        height = shape_params.get("height", 0)
        if base1 < 0 or base2 < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative")
        return 0.5 * (base1 + base2) * height
    
    elif shape_type == "regular_polygon":
        sides = shape_params.get("sides", 3)
        side_length = shape_params.get("side_length", 0)
        if sides < 3:
            raise ValueError("Polygon must have at least 3 sides")
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        return (sides * side_length * side_length) / (4 * math.tan(math.pi / sides))
    
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == "__main__":
    circle_data = {"type": "circle", "radius": 5}
    rectangle_data = {"type": "rectangle", "width": 4, "height": 7}
    triangle_data = {"type": "triangle", "base": 10, "height": 6}
    trapezoid_data = {"type": "trapezoid", "base1": 3, "base2": 7, "height": 4}
    polygon_data = {"type": "regular_polygon", "sides": 6, "side_length": 2}

    print(calculate_area(circle_data))
    print(calculate_area(rectangle_data))
    print(calculate_area(triangle_data))
    print(calculate_area(trapezoid_data))
    print(calculate_area(polygon_data))