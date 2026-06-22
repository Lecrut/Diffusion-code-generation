import math

def calculate_area(shape_params):
    shape_type = shape_params.get("type")
    
    if shape_type == "circle":
        radius = shape_params.get("radius")
        if radius is None or radius < 0:
            raise ValueError("Circle requires a non-negative radius")
        return math.pi * (radius ** 2)
    
    elif shape_type == "rectangle":
        width = shape_params.get("width")
        height = shape_params.get("height")
        if width is None or height is None or width < 0 or height < 0:
            raise ValueError("Rectangle requires non-negative width and height")
        return width * height
    
    elif shape_type == "triangle":
        base = shape_params.get("base")
        height = shape_params.get("height")
        if base is None or height is None or base < 0 or height < 0:
            raise ValueError("Triangle requires non-negative base and height")
        return 0.5 * base * height
    
    elif shape_type == "square":
        side = shape_params.get("side")
        if side is None or side < 0:
            raise ValueError("Square requires a non-negative side")
        return side ** 2
    
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    circle_area = calculate_area({"type": "circle", "radius": 5})
    print(f"Circle area: {circle_area}")
    
    rect_area = calculate_area({"type": "rectangle", "width": 4, "height": 6})
    print(f"Rectangle area: {rect_area}")
    
    triangle_area = calculate_area({"type": "triangle", "base": 3, "height": 7})
    print(f"Triangle area: {triangle_area}")
    
    square_area = calculate_area({"type": "square", "side": 4})
    print(f"Square area: {square_area}")