import math

def calculate_area(shape_params):
    shape_type = shape_params.get("shape")
    
    if shape_type == "circle":
        radius = shape_params.get("radius")
        if radius is None or radius <= 0:
            raise ValueError("Circle requires a positive radius")
        return math.pi * (radius ** 2)
    
    elif shape_type == "rectangle":
        width = shape_params.get("width")
        height = shape_params.get("height")
        if width is None or height is None or width <= 0 or height <= 0:
            raise ValueError("Rectangle requires positive width and height")
        return width * height
    
    elif shape_type == "triangle":
        base = shape_params.get("base")
        height = shape_params.get("height")
        if base is None or height is None or base <= 0 or height <= 0:
            raise ValueError("Triangle requires positive base and height")
        return 0.5 * base * height
    
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    circle_params = {"shape": "circle", "radius": 5}
    rectangle_params = {"shape": "rectangle", "width": 4, "height": 6}
    triangle_params = {"shape": "triangle", "base": 10, "height": 3}
    
    print(calculate_area(circle_params))
    print(calculate_area(rectangle_params))
    print(calculate_area(triangle_params))