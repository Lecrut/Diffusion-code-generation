import math

def calculate_area(shape_data: dict) -> float:
    shape_type = shape_data.get("type")
    
    if shape_type == "circle":
        radius = shape_data.get("radius")
        if radius is None or radius <= 0:
            raise ValueError("Circle requires a positive radius.")
        return math.pi * (radius ** 2)
    
    elif shape_type == "rectangle":
        width = shape_data.get("width")
        height = shape_data.get("height")
        if width is None or height is None or width <= 0 or height <= 0:
            raise ValueError("Rectangle requires positive width and height.")
        return width * height
    
    elif shape_type == "triangle":
        base = shape_data.get("base")
        height = shape_data.get("height")
        if base is None or height is None or base <= 0 or height <= 0:
            raise ValueError("Triangle requires positive base and height.")
        return 0.5 * base * height
    
    elif shape_type == "square":
        side = shape_data.get("side")
        if side is None or side <= 0:
            raise ValueError("Square requires a positive side length.")
        return side ** 2
    
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    circle_data = {"type": "circle", "radius": 5}
    circle_area = calculate_area(circle_data)
    print(circle_area)

    rectangle_data = {"type": "rectangle", "width": 4, "height": 6}
    rectangle_area = calculate_area(rectangle_data)
    print(rectangle_area)

    triangle_data = {"type": "triangle", "base": 10, "height": 8}
    triangle_area = calculate_area(triangle_data)
    print(triangle_area)

    square_data = {"type": "square", "side": 7}
    square_area = calculate_area(square_data)
    print(square_area)