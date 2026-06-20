import math

def calculate_area(shape_data):
    shape_type = shape_data.get("type")
    
    if shape_type == "circle":
        radius = shape_data["radius"]
        return math.pi * (radius ** 2)
    elif shape_type == "rectangle":
        length = shape_data["length"]
        width = shape_data["width"]
        return length * width
    elif shape_type == "triangle":
        base = shape_data["base"]
        height = shape_data["height"]
        return 0.5 * base * height
    elif shape_type == "square":
        side = shape_data["side"]
        return side ** 2
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")

if __name__ == '__main__':
    circle_params = {"type": "circle", "radius": 5}
    rectangle_params = {"type": "rectangle", "length": 10, "width": 4}
    triangle_params = {"type": "triangle", "base": 6, "height": 8}
    square_params = {"type": "square", "side": 7}

    print(calculate_area(circle_params))
    print(calculate_area(rectangle_params))
    print(calculate_area(triangle_params))
    print(calculate_area(square_params))