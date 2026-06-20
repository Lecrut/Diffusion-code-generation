def calculate_area(shape_params):
    shape_type = shape_params.get("type")
    
    if shape_type == "rectangle":
        width = shape_params.get("width", 0)
        height = shape_params.get("height", 0)
        return width * height
    elif shape_type == "circle":
        radius = shape_params.get("radius", 0)
        return 3.14159265359 * radius * radius
    elif shape_type == "triangle":
        base = shape_params.get("base", 0)
        height = shape_params.get("height", 0)
        return 0.5 * base * height
    elif shape_type == "square":
        side = shape_params.get("side", 0)
        return side * side
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == "__main__":
    rectangle_params = {"type": "rectangle", "width": 5, "height": 10}
    circle_params = {"type": "circle", "radius": 3}
    triangle_params = {"type": "triangle", "base": 6, "height": 4}
    square_params = {"type": "square", "side": 7}
    
    print(calculate_area(rectangle_params))
    print(calculate_area(circle_params))
    print(calculate_area(triangle_params))
    print(calculate_area(square_params))